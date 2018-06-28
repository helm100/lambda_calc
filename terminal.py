#!/usr/bin/env python3

from Class_Lambda import functie
from Class_Lambda import expr
from str_to_expr import str_to_expr

print("Welcome..")
print("To enter and evaluate lambda expressions, type 'lambda'.")
print("To use a calculator that is programmed with lambda calculus, type 'calc'.")
print("To exit, type exit.")


def menu(input_user): #basismenu
	if input_user == "lambda":
		print("You can enter a lambda expression to be evaluated.")
		print("You can check whether two expressions are equal with ==")
		print("To go back, type 'back'. To exit, type 'exit'.")
		lambda_evaluator(input("type a lambda expression: "))
	elif input_user == "calc":
		lambda_calculator(input("type a simple calculation: "))
	elif input_user == "exit":
		return None
	else:
		menu(input("type lambda, calc or exit: "))
		
def lambda_evaluator(user_input): #neemt als input een lambda expr en evalueert/vergelijkt deze
	if user_input == "back":
		menu(input("type lambda, calc or exit: "))
	elif user_input == "exit":
		return None
	else:
		l_expr = str_to_expr(user_input)
		print("Your lambda expression: "+str(l_expr))
		l_expr.eval_subexpr()
		#while l_expr[0].body.bevat_functie(): #de vereenvoudig functie moet beter, moet zoiets bevatten maar ook stoppen na een aantal pogingen
		#	l_expr.vereenvoudig()
		print("In simplified form: "+str(l_expr))
		lambda_evaluator(input("type a lambda expression: "))
	
sucs = str_to_expr("(lxyz.y(xyz))")
pred = None #predecessor
#oprt = {'+': str_to_expr("(lxyz.y(xyz))"),'-': str_to_expr("(lxy.yPx)"),'*': str_to_expr("(lxyz.x(yz))")}	

def lambda_calculator(user_input): #zet input zoals '2+3' om in een lambda expr en evalueert deze
	if user_input == "back":
		menu(input("type lambda, calc or exit: "))
	elif user_input == "exit":
		return None
	try:
		exprs=[]
		for i in range(len(user_input)):
			if user_input[i] == '+':
				exprs.append(numb_to_lamb(user_input[:i]))
				exprs.append(sucs[0])
				exprs.append(numb_to_lamb(user_input[i+1:]))
				exprs = expr(exprs)
				break
		print("In lambda form: "+str(exprs))
		exprs.eval_subexpr()
		#for i in range(80): #ik laat hem nu gewoon 80 keer vereenvoudigen, kan handiger misschien
		#	exprs.vereenvoudig()
		exprs.vereenvoudig()
		print("Simplified: "+str(exprs))
		print("In human language: "+str(count(exprs[0].body)))
		lambda_calculator(input("type a simple calculation: "))
	except ValueError:
		print("I couldn't interpret this, sorry")
		lambda_calculator(input("type a simple calculation: "))
		
def numb_to_lamb(numberstr): #zet een geheel getal om in een lambdafunctie	
	n = int(numberstr)
	l_str = "(lsz."
	for i in range(n):
		l_str += "s("
	l_str += "z"+")"*(n+1)
	return str_to_expr(l_str)[0]
	
def calc_to_lamb(input, exprs=[]): #zet een berekening om in lambda expressie
	for i in range(len(input)):
		base=0
		if input[i] == "(":
			exprs.append(calc_to_lamb(input[i+1:],[]))
		elif input[i] == "+":
			exprs.append(numb_to_lamb(input[base:i]))
			exprs.append(pls)
			base = i+1
		elif input[i] == "-":
			pass
		elif input[i] == "*":
			pass
		elif input[i] == ")":
			return exprs
		elif i == len(input)-1:
			exprs.append(numb_to_lamb(input[base:i]))
			return expr(exprs)
			
def count(lijst,n=0,ref=None): #telt het aantal sublijsten om een lambda functie om te zetten naar een geheel getal
		for x in lijst:
			if n==0 and ref==None:
				ref = x
				n+=1
			elif x==ref:
				n+=1
			elif isinstance(x,list):
				n+=count(x,0,ref)
		return n
				
		
menu(input("type lambda, calc or exit: "))
	

print("Thank you for using me!")

'''lambda_versie_input = ...
print(lambda_versie_input)
gereduceerde_lambda_versie = ...
print(gereduceerde_lambda_versie)
uitkomst = ...
print(uitkomst)
'''
