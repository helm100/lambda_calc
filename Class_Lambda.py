#!/usr/bin/env python3
#from str_to_expr import str_to_expr

import copy
from itertools import chain
#from str_to_expr import str_to_expr

#denk na over invoer van functies zonder haakjes (alfa_reductie)/meerdere variabelen vaker voorkomen
#denk na over len(self.body)==0
#the reduction process may not terminate. For instance, consider the term O = ( lx . x x ) ( l x . x x ), gaat naar zichzelf dus stopt nooit  

#Te doen:
#-andere foute invoer
#-(lx.(ly.xy))ab = (lxy.xy)ab ; dit is belangrijk om vermenigvuldiging te laten werken

alfabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def str_to_expr1(tekst):
	inp = []
	haakjes = 0
	for i in range(len(tekst)):
		if tekst[i] == "l" and haakjes == 0:
			beg = i
			haakjes += 1
		elif tekst[i] == "(" and haakjes > 0:
			haakjes += 1
		elif tekst[i] == ")" and haakjes > 1:
			haakjes -= 1
		elif tekst[i] == ")" and haakjes == 1:
			haakjes -= 1
			nieuwe_tekst=tekst[beg:i+1]
			index=nieuwe_tekst.find('.')
			pram=list(nieuwe_tekst[1:index])
			body=expr1_to_expr(str_to_expr1(nieuwe_tekst[index+1:len(nieuwe_tekst)-1]),[])
			inp.append(functie(pram,body))
		elif haakjes == 0 and not (i<len(tekst)-1 and tekst[i+1]=="l"):
			inp.append(tekst[i])
		
	return inp
	
def expr1_to_expr(input,output=[]):
	if len(input) == 0:
		return output
	if input[0] == ")":
		del input[0]
		return output
	elif input[0] == "(":
		del input[0]
		subl = expr1_to_expr(input,[])
		output.append(subl)
		return expr1_to_expr(input,output)
	else:
		output.append(input.pop(0))
		return expr1_to_expr(input,output)
		
def str_to_expr(tekst): #ik heb hier toegevoegd dat hij er een expressie van maakt
	return expr(expr1_to_expr(str_to_expr1(tekst),[]))

class functie:
	def __init__(self, pram=['x'], body=['x']):
		self.pram=expr(pram)
		self.body=expr(body)


	def __str__(self):
		return "(l" + str(self.pram) + "." + str(self.body) + ")"
	
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

	def voeg_samen(self):
		if not self.body.bevat_functie():
			return self
		else:
			for i in range(len(self.body)):
				if isinstance(self.body[i], functie):
					self.pram = expr(self.pram + self.body[i].pram)
					if self.body[i].body.bevat_functie():
						self.body[i].voeg_samen()
					self.body[:] = self.body[:i] + self.body[i].body + self.body[i+1:]
			return self

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
	
#Deze functie werkt niet als er letters voorkomen die niet in het europese alfabet van kleine letters zitten.	
	def hernoem(self):
		vervangen = []
		string = list(str(self))
		for i in range(len(string)):
			if (string[i] != "(") and (string[i] != ")") and (string[i] != ".") and (string[i] != "l"):
				if string[i] in vervangen:
					string[i] = alfabet[vervangen.index(string[i])]
				else:
					vervangen.append(string[i])
					string[i] = alfabet[len(vervangen)-1]
		self[:] = str_to_expr("".join(string))
		print(self)
		return self

	def __eq__(self,other):
		if type(other) != expr:
			return False
		self.evalueer()
		other.evalueer()
		if len(self)!=len(other):
			return False
		n=0
		self.hernoem()
		other.hernoem()
		for i in range(len(self)):
			if str(self[i])==str(other[i]):
				n += 1
		if len(self)==n:
			return True
		return False





