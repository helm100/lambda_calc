#!/usr/bin/env python3

from Class_Lambda import functie
from Class_Lambda import expr
from Class_Lambda import str_to_expr
import copy

#Als de gebruiker het programma opent wordt hij of zij gelijk op onderstaande manier begroet
print("Welcome..")
print("To enter and evaluate lambda expressions, type 'lambda'.")
print("To use a calculator that is programmed with lambda calculus, type 'calc'.")
print("To quit, type q.")


def menu(input_user): #basismenu
	if input_user == "lambda":
		print("You can enter a lambda expression to be evaluated.")
		print("You can check whether two expressions are equal with ==")
		print("To go back, enter 'b'. To quit, enter 'q'.")
		lambda_evaluator(input("type a lambda expression: "))
	elif input_user == "calc":
		lambda_calculator(input("type a simple calculation: "))
	elif input_user == "q":
		return None
	else:
		menu(input("type lambda, calc or q: "))
		
def lambda_evaluator(user_input): #neemt als input een lambda expr en evalueert/vergelijkt deze
	if user_input == "b":
		menu(input("type lambda, calc or q: "))
	elif user_input == "q":
		return None
	else:
		#try:
			if '==' in user_input:
				indx = user_input.index('=')
				TorF = str_to_expr(user_input[:indx])==str_to_expr(user_input[indx+2:])
				if TorF:
					print("I think these expressions are equivalent.")
				else:
					print("I think these expressions are not equivalent.")
				lambda_evaluator(input("type a lambda expression: "))
			else:
				l_expr = str_to_expr(user_input)
				print("Your lambda expression: "+str(l_expr))
				l_expr.evalueer()
				print("In simplified form: "+str(l_expr))
				lambda_evaluator(input("type a lambda expression: "))
		#except:
		#	print("I could not interpret this, sorry")
		#	lambda_evaluator(input("type a lambda expression: "))
	
sucs = str_to_expr("(lxyz.y(xyz))")[0]
pred = None #predecessor
#oprt = {'+': str_to_expr("(lxyz.y(xyz))"),'-': str_to_expr("(lxy.yPx)"),'*': str_to_expr("(lxyz.x(yz))")}	
tms = str_to_expr("(lxyz.x(yz))")[0]

def lambda_calculator(user_input): #zet input zoals '2+3' om in een lambda expr en evalueert deze
	if user_input == "b":
		menu(input("type lambda, calc or exit: "))
	elif user_input == "q":
		return None
	#try:
	exprs = calc_to_lamb(user_input)
	print("In lambda form: "+str(exprs))
	exprs.evalueer()
	#exprs[0][0].voeg_samen()
	print("Simplified: "+str(exprs))
	try:
		print("In human language: "+str(count(exprs[0])))
		lambda_calculator(input("type a simple calculation: "))
	except:
		print("I couldn't interpret this as a number")
		lambda_calculator(input("type a simple calculation: "))
	#except (ValueError, AttributeError):
	#	print("I couldn't interpret this, sorry")
	#	lambda_calculator(input("type a simple calculation: "))
		
def numb_to_lamb(numberstr): #zet een geheel getal om in een lambdafunctie	
	n = int(numberstr)
	l_str = "(lab."
	for i in range(n):
		l_str += "a("
	l_str += "b"+")"*(n+1)
	return str_to_expr(l_str)[0]
	
def calc_to_lamb(input): #zet een berekening om in lambda expressie
	base=0
	exprs = []
	for i in range(len(input)):
		if input[i] == "(":
			exprs.append(calc_to_lamb(input[i+1:]))
		elif input[i] == "+":
			exprs.append(numb_to_lamb(input[base:i]))
			exprs.append(sucs)
			base = i+1
		elif input[i] == "-":
			pass
		elif input[i] == "*":
			exprs.append([copy.deepcopy(tms),numb_to_lamb(input[base:i])]+calc_to_lamb(input[i+1:]))
			return expr(exprs)
		elif input[i] == ")":
			return exprs
		elif i == len(input)-1:
			exprs.append(numb_to_lamb(input[base:]))
			return expr(exprs)
			
def count(lijst): #deze functie zet een lambda expressie om in een geheel getal
	string = str(lijst)
	ref = string[string.find("l")+1]
	n=0
	for x in string:
		if x == ref:
			n+=1
	return n-1

		
		

#ex = str_to_expr("(lx.(ly.xy))")
#print(ex.vind_vrij())
		
menu(input("type lambda, calc or q: "))
	

#print("Thank you for using me!")


