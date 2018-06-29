#!/usr/bin/env python3
from Class_Lambda import functie
from Class_Lambda import expr
from str_to_expr import str_to_expr

input = "3+5*6"

pls = "plus"
mn = "minus"
tms = "times"

		
def numb_to_lamb(numberstr): #zet een geheel getal om in een lambdafunctie	
	n = int(numberstr)
	l_str = "(lsz."
	for i in range(n):
		l_str += "s("
	l_str += "z"+")"*(n+1)
	return str_to_expr(l_str)[0]
	
def calc_to_lamb(input, exprs=[]):
	base=0
	for i in range(len(input)):
		if input[i] == "(":
			exprs.append(calc_to_lamb(input[i+1:],[]))
		elif input[i] == "+":
			exprs.append(numb_to_lamb(input[base:i]))
			exprs.append(pls)
			base = i+1
		elif input[i] == "-":
			pass
		elif input[i] == "*":
			exprs.append(tms)
			exprs.append(numb_to_lamb(input[base:i]))
			base = i+1
		elif input[i] == ")":
			return exprs
		elif i == len(input)-1:
			exprs.append(numb_to_lamb(input[base:]))
			return expr(exprs)

ex = calc_to_lamb("1+1")
print(ex)





