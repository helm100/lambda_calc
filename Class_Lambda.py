#!/usr/bin/env python3
#from str_to_expr import str_to_expr


#denk na over invoer van functies zonder haakjes (alfa_reductie)/meerdere variabelen vaker voorkomen
#denk na over len(self.body)==0
#the reduction process may not terminate. For instance, consider the term O = ( lx . x x ) ( l x . x x ), gaat naar zichzelf dus stopt nooit  

#deze is wrs niet meer nodig
def replace(lijst, old, new):
	for i in range(len(lijst)):
		if lijst[i] == old:
			lijst[i]=new
	return lijst

class functie:
	def __init__(self, pram=['x'], body=['x']):
		self.pram=pram
		self.body=expr(body)


	def __str__(self):
	
		'''body=[]
		for x in self.body:
			if isinstance(x, functie):
				body.append(x.__str__())
			#elif isinstance(x, lijst):
			#	body.append('('++')')
			else: 
				body.append(x)'''
	
	
		return "(l" + ''.join(self.pram) + "." + str(self.body) + ")"
	
	def alfa_conversion(self):
		pass

	#laatste poppen is wss efficienter
	#misschien wil je de functie verwijderen uit het geheugen als alle variabelen gebruikt zijn
	def beta_redu(self, argumenten):
		while len(argumenten)>0 and len(self.pram)>0:
			#self.body = replace(self.body, self.pram.pop(0), argumenten.pop(0))
			self.body.subst(self.pram.pop(0),argumenten.pop(0))
		if len(self.pram)==0:
			return expr(self.body + argumenten)
		return expr([self])

#error handling voor te diepe recursie
def eval_subexpr(lijst):
	new_list=[]
	for i in range(len(lijst)):
		if isinstance(lijst[i], list):
			if bevat_lijst(lijst[i]):
				new_list += eval_subexpr(lijst[i])
			else:
				new_list += evalueer(lijst[i])
		else:
			new_list.append(lijst[i])
	return evalueer(new_list)
	

	
#eigenlijk willen we dit net iets anders hebben: sublijsten moeten ook weer expressies zijn	
#je kan een expressie printen en elementen substitueren
class expr(list):

	'''def __init__(self,lijst):
		self = []
		for i in range(len(lijst)):
			if isinstance(lijst[i],list):
				self.l.append(expr(self[i]))
			else:
				self.l.append(self[i])'''

	def bevat_lijst(self):
		for x in self:
			if isinstance(x, list):
				return True
		return False

	def bevat_functie(self):
		for x in self:
			if isinstance(x, functie):
				return True
		return False
	
	#Deze functie vervangt in een body (dus een expr) een bepaalde parameter (pram) door other
	def subst(self,pram,other):
		for i in range(len(self)):
			if isinstance(self[i],list): #anders als sublijsten al expr zijn
				self[i]=expr(self[i]).subst(pram,other)
			elif self[i] == pram:
				self[i] = other
		return self

	#deze functie is niet commutatief/houdt geen rekening met haakjes volgorde
	def evalueer(self):
		if len(self) == 1:
			return self
		if isinstance(self[0], functie):
			self[0] = self[0].beta_redu(self[1:]).evalueer()
			for x in range(1, len(self)):
				del self[x]
			return self
		else:
			self = expr([self[0]]) + expr(self[1:]).evalueer()
			return self

	#gemaakt om een body erin te stoppen
	'''def vereenvoudig(self):
		if self.bevat_functie():
			self=eval_subexpr(self)
			return self.vereenvoudig()
		else:
			return self'''

	def __str__(self):
		expressie = []
		for x in self:
			if isinstance(x,list): #anders als sublijsten al expr zijn
				expressie.append('('+str(expr(x))+')')
			else:
				expressie.append(str(x))
		return ''.join(expressie)

