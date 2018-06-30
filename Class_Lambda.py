#!/usr/bin/env python3
#from str_to_expr import str_to_expr

import copy
from itertools import chain

#denk na over invoer van functies zonder haakjes (alfa_reductie)/meerdere variabelen vaker voorkomen
#denk na over len(self.body)==0
#the reduction process may not terminate. For instance, consider the term O = ( lx . x x ) ( l x . x x ), gaat naar zichzelf dus stopt nooit  

#Te doen:
#-locale variabelen/naamgeving
#-andere foute invoer
#-vereenvoudig
#-methode __eq__
#-nu: (lab.ab)b = (lb.bb); moet zijn: (lab.ab)b = (lx.bx)
#-(lx.(ly.xy))ab = (lxy.xy)ab ; dit is belangrijk om vermenigvuldiging te laten werken


class functie:
	def __init__(self, pram=['x'], body=['x']):
		self.pram=expr(pram)
		self.body=expr(body)


	def __str__(self):
		return "(l" + ''.join(self.pram) + "." + str(self.body) + ")"
	
	def alfa_conv(self, nieuwe_var):
		if len(nieuwe_var) != len(self.pram):
			print("Invalid input for alfa conversion.")
		else:
			for i in range(len(self.pram)):
				self.body.subst(self.pram[i],nieuwe_var[i])
			self.pram = list(nieuwe_var)
			return self

	#laatste poppen is wss efficienter
	#misschien wil je de functie verwijderen uit het geheugen als alle variabelen gebruikt zijn
	def beta_redu(self, argumenten):
		while len(argumenten)>0 and len(self.pram)>0:
			self.body.subst(self.pram.pop(0),argumenten.pop(0))
		if len(self.pram)==0:
			return expr(self.body + argumenten)
		return expr([self])

#je kan een expressie printen en elementen substitueren
class expr(list):
	def __init__(self,lijst):
		super().__init__(lijst)
		for i in range(len(self)):
			if isinstance(self[i],list):
				self[i] = expr(self[i])

	def bevat_functie(self): #niet meer nodig?
		for x in self:
			if isinstance(x, functie):
				return True
			elif isinstance(x, expr):
				if x.bevat_functie():
					return True
		return False
	
	#Deze functie vervangt in een body (dus een expr) een bepaalde parameter (pram) door other
	def subst(self,pram,other):
		for i in range(len(self)):
			if isinstance(self[i], expr):
				self[i]=self[i].subst(pram,other)
			elif isinstance(self[i], functie):
				self[i].body=self[i].body.subst(pram, other)
				self[i].pram=self[i].pram.subst(pram, other)
			elif self[i] == pram:
				self[i] = copy.deepcopy(other) #hier moeten de functies onafhankelijk zijn
		return self

	#Is alles een expr of wordt dat nu te vaak gedaan?
	#nu wordt bij een error wel een lege lijst gereturnd
	def evalueer(self):
		try:
			if len(self)==1:
				if isinstance(self[0],expr): #met deze situatie hield hij eerst geen rekening
					self[0].evalueer()
				return self
			if isinstance(self[0], expr):
				self[0] = self[0].evalueer()
				self[:] = expr(chain.from_iterable([self[0], self[1:]])) #ik heb [:] toegevoegd
				self.evalueer()
				return self
			elif isinstance(self[0], functie):
				self[:]=self[0].beta_redu(self[1:]).evalueer()
				if isinstance(self[0], functie):
					if self[0].body.bevat_functie():
						self[0].body=self[0].body.evalueer() #hier stond eerst self[0]=self[0].body...
				return expr(self)
			elif isinstance(self[0], str):
				self[1:]=expr(self[1:]).evalueer()
				return expr(self)
			else:
				print("Invalid input! This type: " + type(self[0]).__name__ + ", should not be in an expression.")
				return None
		except RecursionError:
			print("This expression can not be evaluated and will go on for ever.")
			return self
	
	def __str__(self):
		expressie = []
		for x in self:
			if isinstance(x,expr): 
				expressie.append('('+str(x)+')')
			else:
				expressie.append(str(x))
		return ''.join(expressie)
		
	def __eq__(self,other):
		if type(other) != expr:
			return False
		self.evalueer()
		other.evalueer()
		if len(self)!=len(other):
			return False
		n=0
		for i in range(len(self)):
			if str(self[i])==str(other[i]):
				n += 1
		if len(self)==n:
			return True
		return False
		
