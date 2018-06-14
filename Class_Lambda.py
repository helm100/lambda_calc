#!/usr/bin/env python3
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
			self.body=evalueer(self.body)
			return self.vereenvoudig()
		else:
			return self

#Volgens mij kunnen we deze functie ook als een methode maken met overloaden, alleen ik wist ff niet hoe
#Deze functie neemt een string en returnd de bijpassende functie
def str_to_func(tekst):
	if tekst[0]=="(" and tekst[-1]==")":
		begin=2
	else:
		begin=1
	index = tekst.find(".")
	pram=[]
	body=[]
	for x in range(begin,index):
		pram.append(tekst[x])
	for x in range(index+1,len(tekst)+1-begin):
		body.append(tekst[x])
	return functie(pram, body)
	

def str_to_expr(tekst):
	output = []
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
			#func = verw_haak(tekst[beg:i+1])
			nieuwe_tekst=tekst[beg:i+1]
			index=nieuwe_tekst.find('.')
			pram=list(nieuwe_tekst[1:index])
			body=str_to_expr(nieuwe_tekst[index+1:len(nieuwe_tekst)-1])
			output.append(functie(pram,body))
		elif haakjes == 0:
			output.append(tekst[i])
	return output

#deze functie is niet commutatief/houdt geen rekening met haakjes volgorde
def evalueer(lijst):
	if len(lijst) == 1:
		return lijst
	if isinstance(lijst[0], functie):
			return evalueer(lijst[0].beta_redu(lijst[1:]))
	else:
		return [lijst[0]]+evalueer(lijst[1:])

expr = str_to_expr("(lxyz.y(xyz))((lxyz.y(xyz))(luv.u(u(uv))))")
#expr = [expr[0]] + evalueer([expr[1], expr[2]])
print(expr[1])



