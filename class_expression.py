#!/usr/bin/env python3

#vooralsnog staat deze klasse ook in Class_Lambda.py

from Class_Lambda import functie

class expr(list):

	'''def __init__(self,lijst):
		self = []
		for i in range(len(lijst)):
			if isinstance(lijst[i],list):
				self.l.append(expr(self[i]))
			else:
				self.l.append(self[i])'''
	
	def subst(self,pram,other):
		for i in range(len(self)):
			if isinstance(self[i],list): #anders als sublijsten al expr zijn
				self[i]=expr(self[i]).subst(pram,other)
			elif self[i] == pram:
				self[i] = other
		return self

	def __str__(self):
		expressie = []
		for x in self:
			if isinstance(x,list): #anders als sublijsten al expr zijn
				expressie.append('('+str(expr(x))+')')
			else:
				expressie.append(str(x))
		return ''.join(expressie)

func = functie(['a','b'],['a',['b','c']])