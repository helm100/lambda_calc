#!/usr/bin/env python3
#from str_to_expr import str_to_expr


#denk na over invoer van functies zonder haakjes (alfa_reductie)
#denk na over len(self.body)==0
#the reduction process may not terminate. For instance, consider the term O = ( lx . x x ) ( l x . x x ), gaat naar zichzelf dus stopt nooit  
def replace(lijst, old, new):
	for i in range(len(lijst)):
		if lijst[i] == old:
			lijst[i]=new
	return lijst

#Voeg toe dat pram, body niet leeg zijn
class functie:
	def __init__(self, pram, body):
		self.pram=pram
		self.body=body

#laten we lambda als een l printen
	def __str__(self):
		body=[]
		for x in self.body:
			if isinstance(x, functie):
				body.append(x.__str__())
			else: 
				body.append(x)
		
		return "(l" + ''.join(self.pram) + "." + "".join(body) + ")"

	def alfa_conversion(self):
		pass

	#laatste poppen is wss efficienter
	def beta_redu(self, argumenten):
		while len(argumenten)>0 and len(self.pram)>0:
			self.body = replace(self.body, self.pram.pop(0), argumenten.pop(0))
		if len(self.pram)==0:
			return self.body + argumenten
		return [self]

	def body_bevat_functie(self):
		for x in self.body:
			if isinstance(x, functie):
				return True
		return False

	#gemaakt om een body erin te stoppen
	def vereenvoudig(self):
		if self.body_bevat_functie():
			self.body=eval_subexpr2(self.body)
			return self.vereenvoudig()
		else:
			return self

#deze functie is niet commutatief/houdt geen rekening met haakjes volgorde
def evalueer(lijst):
	if len(lijst) == 1:
		return lijst
	if isinstance(lijst[0], functie):
			return evalueer(lijst[0].beta_redu(lijst[1:]))
	#elif isinstance(lijst[0], list):
	#	return evalueer(evalueer(lijst[0])
	else:
		return [lijst[0]]+evalueer(lijst[1:])

def bevat_lijst(lijst):
	for x in lijst:
		if isinstance(x, list):
			return True
	return False

#error handling voor te diepe recursie
def eval_subexpr(lijst):
	if len(lijst)==0:
		return []
	if not bevat_lijst(lijst):
		return evalueer(lijst)
	if isinstance(lijst[0], list):
		return eval_subexpr(lijst[0])+eval_subexpr(lijst[1:])
	else:
		return [lijst[0]]+eval_subexpr(lijst[1:])

def eval_subexpr2(lijst):
	new_list=[]
	for i in range(len(lijst)):
		#print(new_list)
		if isinstance(lijst[i], list):
			#print(lijst[i])
			if bevat_lijst(lijst[i]):
				new_list += eval_subexpr2(lijst[i])
			else:
				new_list += evalueer(lijst[i])
		else:
			new_list.append(lijst[i])
	return evalueer(new_list)

functie1=functie(["a", "b"], ["b"])
functie2=functie(["x", "y", "z"], ["x", "y", "z", "z"])
functie3=functie(["q"], ["q", "q"])
#expr=["b", "x", "y", "z",[functie2,[[functie1,"q"],functie3]], "a"]

'''for x in evalueer(eval_subexpr2(expr)):
	if isinstance(x, functie):
		print(x.vereenvoudig())
	else:
		print(x)'''


'''expr_2=[functie2,[functie1,functie3]]
for x in eval_subexpr2(expr_2):
	print(x)'''



#print(eval_subexpr2(expr)[0].body[0].body,[])


'''for x in evalueer(expr):
	print(x)'''
'''for x in eval_subexpr2(expr):
	if isinstance(x, functie):
		print(x.vereenvoudig())
	else:
		print(x)'''




