#!/usr/bin/env python3
from Class_Lambda import functie
from Class_Lambda import expr
from str_to_expr import str_to_expr


pls = "plus"
mn = "minus"
tms = str_to_expr("(lxyz.x(yz))")[0]

def numb_to_lamb(numberstr): #zet een geheel getal om in een lambdafunctie	
	n = int(numberstr)
	l_str = "(lsz."
	for i in range(n):
		l_str += "s("
	l_str += "z"+")"*(n+1)
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
			exprs.append([tms,numb_to_lamb(input[base:i])]+calc_to_lamb(input[i+1:]))
			return expr(exprs)
		elif input[i] == ")":
			return exprs
		elif i == len(input)-1:
			exprs.append(numb_to_lamb(input[base:]))
			return expr(exprs)

def count(lijst):
	string = str(lijst)
	if string[1] != 'l':
		ref = string[0]
	else:
		ref = string[4]
		print(ref)
	n=0
	for x in string:
		if x == ref:
			n+=1
	return n
				
		
#input = "2*3"
#ex = calc_to_lamb(input)
ex1 = str_to_expr("(lpqr.p(qr))(lsz.s(sz))(lab.a(a(ab)))")
ex2 = str_to_expr("(labc.a(bc))(lsz.s(sz))(lxy.x(x(xy)))")
ex1.evalueer()
ex2.evalueer()
print(ex1)
print(ex2)





