#!/usr/bin/env python3
'''
Dit programma biedt de mogelijkheid om interactief lambda expressies
in te voeren en geeft dan de gereduceerde expressies terug.
Ook kunnen er basisberekeningen mee worden uitgevoerd met 
optellen en vermenigvuldigen. Deze berekeningen worden volledig met
behulp van de lambdacalculus uitgevoerd.
'''

from Class_Lambda import functie
from Class_Lambda import expr
from Class_Lambda import str_to_expr
import copy

#welkomswoorden
print("Welcome..")
print("To enter and evaluate lambda expressions, type 'lambda'.")
print("To use a calculator that is programmed with lambda calculus, type 'calc'.")
print("To quit, type q.")


def menu(input_user): #basismenu
	if input_user == "lambda":
		print("You can enter a lambda expression to be evaluated.")
		print("You can check whether two expressions are equal with ==")
		print("To go back, enter 'b'. To quit, enter 'q'.")
		lambda_evaluator(input("type a lambda expression: ")) #wordt doorgestuurd naar lambda_evaluator
	elif input_user == "calc":
		print("You can enter calculations like 2+2, 3*4, 3+6*2.")
		print("We have no support for subtraction or for calculations like 2+2+3")
		lambda_calculator(input("type a simple calculation: ")) ##wordt doorgestuurd naar lambda_calculator
	elif input_user == "q":
		return None #het programma geeft een output en heeft geen vervolgstap meer en sluit dus af
	else:
		menu(input("type lambda, calc or q: "))
		
def lambda_evaluator(user_input): #neemt als input een lambda expr en evalueert/vergelijkt deze
	if user_input == "b":
		menu(input("type lambda, calc or q: ")) #terug naar menu
	elif user_input == "q":
		return None #het programma stopt hierna, zoals hierboven
	else:
		try:
			if '==' in user_input: #vergelijk beide expressies
				indx = user_input.index('=')
				TorF = str_to_expr(user_input[:indx])==str_to_expr(user_input[indx+2:])
				if TorF:
					print("I think these expressions are equivalent.")
				else:
					print("I think these expressions are not equivalent.")
				lambda_evaluator(input("type a lambda expression: "))
			else:
				l_expr = str_to_expr(user_input) #zet input om naar expressie en evalueer
				print("Your lambda expression: "+str(l_expr))
				l_expr.evalueer()
				print("In simplified form: "+str(l_expr))
				lambda_evaluator(input("type a lambda expression: "))
		except:
			print("I could not interpret this, sorry")
			lambda_evaluator(input("type a lambda expression: "))
	
#verschillende veelgebruikte lambda functies
sucs = str_to_expr("(lxyz.y(xyz))")[0] #successor
tms = str_to_expr("(lxyz.x(yz))")[0] #multiplier
T = str_to_expr("(lxy.x)")[0] #TRUE
F = str_to_expr("(lxy.y)")[0] #FALSE
A = str_to_expr("(lxy.xy(luv.v))")[0] #AND
O = str_to_expr("(lxy.x(luv.u)y)")[0] #OR
N = str_to_expr("(lx.x(luv.v)(lab.a))")[0] #NOT


def lambda_calculator(user_input): #zet input zoals '2+3' om in een lambda expr en evalueert deze
	if user_input == "b":
		menu(input("type lambda, calc or exit: ")) #terug naar menu
	elif user_input == "q":
		return None #sluit programma
	try:
		exprs = calc_to_lamb(user_input) #calc_to_lamb is hieronder gedefinieerd en zet een rekensom om naar een lambda expressie
		print("In lambda form: "+str(exprs))
		exprs.evalueer() #vereenvoudig de ingevoerde expressie
		print("Simplified: "+str(exprs))
		try:
			print("In human language: "+str(count(exprs[0]))) #laat uitkomst zien
			lambda_calculator(input("type a simple calculation: "))
		except:
			print("I couldn't interpret this as a number")
			lambda_calculator(input("type a simple calculation: "))
	except (ValueError, AttributeError):
		print("I couldn't interpret this, sorry")
		lambda_calculator(input("type a simple calculation: "))
		
def numb_to_lamb(numberstr): #zet een geheel getal om in een lambdafunctie	
	n = int(numberstr)
	l_str = "(lab."
	for i in range(n):
		l_str += "a(" #bij n=2 wordt er twee keer 'a(' aand '(lab.' geplakt: '(lab.a(a('
	l_str += "b"+")"*(n+1) #afronding: een b en het goede aantal haakjes worden toegevoegd
	return str_to_expr(l_str)[0]
	
def calc_to_lamb(input): #zet een berekening om in lambda expressie
	base=0
	exprs = []
	for i in range(len(input)):
		if input[i] == "(":
			exprs.append(calc_to_lamb(input[i+1:]))
		elif input[i] == "+":
			exprs.append(numb_to_lamb(input[base:i]))
			exprs.append(copy.deepcopy(sucs))
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
	ref = string[string.find("l")+1] #vanaf de eerste l selecteert hij de referentie variabele die hij gaat tellen
	n=0
	for x in string:
		if x == ref:
			n+=1
	return n-1

		
		
menu(input("type lambda, calc or q: "))
	

print("Thank you for using me!")


