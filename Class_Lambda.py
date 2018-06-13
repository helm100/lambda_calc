#denk na over invoer van functies zonder haakjes (alfa_reductie)
#denk na over len(self.body)==0

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
		return "(l" + ''.join(self.pram) + "." + "".join(self.body) + ")"

	def alfa_conversion(self):
		pass

	def beta_redu(self, argumenten):
		while len(argumenten)>0 and len(self.pram)>0:
			self.body = replace(self.body, self.pram.pop(0), argumenten.pop(0))
		if len(self.pram)==0:
			return self.body + argumenten
		return self

	def vereenvoudig():
		pass

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
	
def verw_haak(tekst):
	zonder_haak = ""
	for c in tekst:
		if c != "(" and c != ")":
			zonder_haak += c
	return zonder_haak

def str_to_expr(tekst):
	output = []
	haakjes = 0
	for i in range(len(tekst)):
		if tekst[i] == "(" and haakjes == 0:
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
			pram=list(nieuwe_tekst[2:index])
			body=str_to_expr(nieuwe_tekst[index+1:len(nieuwe_tekst)-1]
			func = functie(pram,body)
			output.append(func)
		elif haakjes == 0:
			output.append(tekst[i])
	return output

def first_functie(lijst):
	for x in range(len(lijst)):
		if isinstance(lijst[x], functie):
			return x
	return None

#Gegeven een lijst met functies en variabelen, evalueer deze helemaal
def evalueer(lijst):
	index = first_functie(lijst)
	if index==None:
		return lijst
	return lijst[:index] + evalueer(lijst[index].beta_redu(lijst[index+1:]))

functie1 = functie(["zx"], ["x"])
functie2 = functie(["y"], ["y"])

lijst = [functie1, "a",functie2]
print(evalueer(lijst))


