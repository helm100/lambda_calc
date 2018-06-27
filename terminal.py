#!/usr/bin/env python3

from Class_Lambda import functie
from Class_Lambda import expr
from str_to_expr import str_to_expr

print("Welcome..")
print("To enter and evaluate lambda expressions, type 'lambda'.")
print("To use a calculator that is programmed with lambda calculus, type 'calc'.")
print("To exit, type exit.")


def menu(input_user):
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
		
def lambda_evaluator(user_input):
	if user_input == "back":
		menu(input("type lambda, calc or exit: "))
	elif user_input == "exit":
		return None
	else:
		l_expr = str_to_expr(user_input)
		print("Your lambda expression: "+str(l_expr))
		print("In simplified form: "+str(l_expr.eval_subexpr()))
		lambda_evaluator(input("type a lambda expression: "))
	
sucs = str_to_expr("(lxyz.y(xyz))")
pred = None #predecessor
#oprt = {'+': str_to_expr("(lxyz.y(xyz))"),'-': str_to_expr("(lxy.yPx)"),'*': str_to_expr("(lxyz.x(yz))")}	

def lambda_calculator(user_input):
	if user_input == "back":
		menu(input("type lambda, calc or exit: "))
	elif user_input == "exit":
		return None
	
	exprs=[]
	for i in range(len(user_input)):
		if user_input[i] == '+':
			exprs.append(numb_to_lamb(user_input[:i]))
			exprs.append(sucs[0])
			exprs.append(numb_to_lamb(user_input[i+1:]))
			exprs = expr(exprs)
			break
	exprs.eval_subexpr()
	print(exprs)
	lambda_calculator(input("type a simple calculation: "))
			
def numb_to_lamb(numberstr):
	n = int(numberstr)
	l_str = "(lsz."
	for i in range(n):
		l_str += "s("
	l_str += "z"+")"*(n+1)
	return str_to_expr(l_str)[0]
		
		
menu(input("type lambda, calc or exit: "))
	

print("Thank you for using me!")

'''lambda_versie_input = ...
print(lambda_versie_input)
gereduceerde_lambda_versie = ...
print(gereduceerde_lambda_versie)
uitkomst = ...
print(uitkomst)
'''
