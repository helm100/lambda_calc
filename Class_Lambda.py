#!/usr/bin/env python3
#from str_to_expr import str_to_expr


#denk na over invoer van functies zonder haakjes (alfa_reductie)
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
		return [self]

	def body_bevat_functie(self):
		for x in self.body:
			if isinstance(x, functie):
				return True
		return False

	#gemaakt om een body erin te stoppen
	def vereenvoudig(self):
		if self.body_bevat_functie():
			self.body=eval_subexpr(self.body)
			return self.vereenvoudig()
		else:
			return self


			
			
def bevat_lijst(lijst):
	for x in lijst:
		if isinstance(x, list):
			return True
	return False
			
#deze functie is niet commutatief/houdt geen rekening met haakjes volgorde
def evalueer(lijst):
	if len(lijst) == 1:
		return lijst
	if isinstance(lijst[0], functie):
			return evalueer(lijst[0].beta_redu(lijst[1:]))
	else:
		return [lijst[0]]+evalueer(lijst[1:])

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

		
	

	
	
	
	
	
'''	

functie1=functie(["a", "b"], ["b"])
functie2=functie(["x", "y", "z"], ["x", "y", "z", "z"])
functie3=functie(["q"], ["q", "q"])
#expr=["b", "x", "y", "z",[functie2,[[functie1,"q"],functie3]], "a"]

for x in evalueer(eval_subexpr(expr)):
	if isinstance(x, functie):
		print(x.vereenvoudig())
	else:
		print(x)


expr_2=[functie2,[functie1,functie3]]
for x in eval_subexpr(expr_2):
	print(x)



#print(eval_subexpr2(expr)[0].body[0].body,[])

for x in evalueer(expr):
	print(x)
for x in eval_subexpr(expr):
	if isinstance(x, functie):
		print(x.vereenvoudig())
	else:
		print(x)


'''

