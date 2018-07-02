#!/usr/bin/env python3

import copy
from itertools import chain

#Deze lijst wordt gebruikt door de methode hernoem om bepaalde gebonden variabelen te hernoemen.
#Deze lijst bevat alle kleine en grote letters van het alfabet behalve de kleine letter l.
alfabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#Deze functie neemt een string als argument en maakt er een lijst met functies, letters en haakjes van.
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

#Deze functie neemt de lijst met functies, letters en haakjes en maakt van gebieden omgeven door extra haakjes sub-expressies.
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
		
#Deze functie past eerst str_to_expr1 toe en vervolgens expr1_to_expr, van de uitkomst wordt een expr gemaakt
#Hierdoor wordt de code een stuk leesbaarder en worden enkele problemen met recursie vermeden
def str_to_expr(tekst):
	return expr(expr1_to_expr(str_to_expr1(tekst),[]))

#Deze klasse wordt gebruikt om functies te definiëren.
class functie:

	#Een functie is simpelweg een lijst met parameters en een lijst met een body
	#Merk op dat self.pram en self.body expressies zijn
	#Als er geen pram en body als argument worden gegeven is de default de identiteitsfunctie
	def __init__(self, pram=['x'], body=['x']):
		self.pram=expr(pram)
		self.body=expr(body)

	#Deze methode geeft de string weergave van een functie terug
	#Merk op dat voor self.pram en self.body de str methode van de klasse expr wordt gebruikt
	def __str__(self):
		return "(l" + str(self.pram) + "." + str(self.body) + ")"
	
	#Deze methode vervangt alle gebonden variabelen van een functie door nieuwe in de lijst nieuwe_var
	#Deze methode wordt gebruikt door de methode evalueer van de expr klasse
	def alfa_conv(self, nieuwe_var):
		if len(nieuwe_var) != len(self.pram):
			print("Invalid input for alfa conversion.")
		else:
			for i in range(len(self.pram)):
				self.body.subst(self.pram[i],nieuwe_var[i])
			self.pram = expr(list(nieuwe_var))
			return self


	#Deze methode past een bepaalde functie (self) toe op een lijst argumenten, oftewel beta-reductie
	#Deze methode wordt gebruikt door de methode evalueer van de expr klasse
	def beta_redu(self, argumenten):
		vervangers = [x for x in alfabet if x not in (self.pram + self.body.vind_vrij(self.pram))]
		while len(argumenten)>0 and len(self.pram)>0:
			if argumenten[0] in self.pram:
				indx = self.pram.index(argumenten[0])
				nieuw_var = self.pram[:indx]+[vervangers.pop(0)]+self.pram[indx+1:]
				self.alfa_conv(nieuw_var)
			self.body.subst(self.pram.pop(0),argumenten.pop(0))
		if len(self.pram)==0:
			return expr(self.body + argumenten)
		return expr([self])

	#Deze methode werkt alleen als hij wordt toegepast nadat een functie en de body ervan helemaal geevalueerd zijn
	#Deze methode wordt gebruikt in evalueer
	def voeg_samen(self):
		if not self.body.bevat_functie():
			return self
		else:
			for i in range(len(self.body)):
				if isinstance(self.body[i], functie):
					if self.body[i].body.bevat_functie():
						self.body[i].voeg_samen()
					self.pram = expr(self.pram + self.body[i].pram)
					self.body[:] = self.body[:i] + self.body[i].body + self.body[i+1:]
			return self

#Deze klasse wordt gebruikt om lambda-expressies te definieren
#Deze klasse erft van de klasse list en is in essentie een lijst variabele, functies en sub-expressies met enkele methodes toegevoegd
class expr(list):

	#Met behulp van de super functie wordt bijne de __init__ van de klasse lijst overgenomen
	#Het verschil is dat van alle sub-lijsten ook expressies worden gemaakt, zodat de methodes van die klasse daar ook op werken
	def __init__(self,lijst):
		super().__init__(lijst)
		for i in range(len(self)):
			if isinstance(self[i],list):
				self[i] = expr(self[i])

	#Deze methode geeft de string weergave van een expressie terug
	#Merk op dat hij gebruik maakt van de __str__ methode van de functie klasse
	def __str__(self):
		expressie = []
		for x in self:
			if isinstance(x,expr): 
				expressie.append('('+str(x)+')')
			else:
				expressie.append(str(x))
		return ''.join(expressie)

	#Deze methode geeft True terug als een expressie of een sub-expressie een functie bevat
	#Deze methode wordt gebruikt door de methode voeg_samen van de functie klasse
	def bevat_functie(self):
		for x in self:
			if isinstance(x, functie):
				return True
			elif isinstance(x, expr):
				if x.bevat_functie():
					return True
		return False
	
	#Deze methode geeft een lijst terug met alle (vrije) variabelen ongelijk aan gebonden van alle functies in een expressie
	def vind_vrij(self,gebonden=[]): 
		vrij = []
		for x in self:
			if isinstance(x,functie):
				vrij += x.body.vind_vrij(gebonden+x.pram)
			elif isinstance(x,expr):
				vrij += x.vind_vrij(gebonden)
			else:
				if x not in gebonden+vrij:
					vrij.append(x)
		return vrij
	
	#Deze methode vervangt in een expressie en de sub-expressies daarvan een bepaalde parameter (param) door other
	#Merk op dat in functies alleen de vrije variabele worden vervangen
	def subst(self,param,other):
		for i in range(len(self)):
			if isinstance(self[i], expr):
				self[i]=self[i].subst(param,other)
			elif isinstance(self[i], functie):
				if param in self[i].body.vind_vrij(self[i].pram): #substitueert vrije var. in een functie
					self[i].body.subst(param,other)
			elif self[i] == param:
				self[i] = copy.deepcopy(other) #hier moeten de functies onafhankelijk zijn
		return self

	#Deze methode evalueerd en vereenvoudigt een expressie compleet, hievoor maakt het gebruik van enkele andere methodes
	def evalueer(self):
		try:
			if len(self)==1:
				if isinstance(self[0],expr):
					self[:] = self[0].evalueer()
				if isinstance(self[0],functie):
					self[0].body.evalueer()
					self[0]=self[0].voeg_samen()
				return self
			if isinstance(self[0], expr):
				self[0] = self[0].evalueer()
				self[:] = expr(chain.from_iterable([self[0], self[1:]])) 
				self.evalueer()
				return self
			elif isinstance(self[0], functie):
				self[:]=self[0].beta_redu(self[1:]).evalueer()
				if isinstance(self[0], functie):
					self[0].body=self[0].body.evalueer()
					self[0] = self[0].voeg_samen()
				return expr(self)
			elif isinstance(self[0], str):
				self[1:]=expr(self[1:]).evalueer()
				return expr(self)
			else:
				print("Invalid input! This type: " + type(self[0]).__name__ + ", should not be in an expression.")
				return None
		except RecursionError: 
			print("The evaluation doesn't terminate, here's what I got:")
			return self

	#Deze methode hernoemt van alle functies in een expressie en de sub-expressies daarvan alle gebonden variabelen zodat twee lambda expressies vergeleken kunnen worden
	#Deze methode werkt niet als er meer dan 51 variabele voorkomen in en expressie
	def hernoem(self): 
		for i in range(len(self)):
			if isinstance(self[i],functie):
				self[i].alfa_conv(alfabet[:len(self[i].pram)])
			elif isinstance(self[i],expr):
				self[i].hernoem()
		return self

	#Deze functie bepaalt de expressies self en other hetzelfde zijn volgens de regels van de lambdacalculus
	def __eq__(self,other):
		if type(other) != expr:
			return False
		self.evalueer()
		other.evalueer()
		if len(self)!=len(other):
			return False
		self = self.hernoem()
		other = other.hernoem()
		for i in range(len(self)):
			if str(self[i])!=str(other[i]):
				return False
		return True

