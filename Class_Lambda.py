#denk na over invoer van functies zonder haakjes (alfa_reductie)

def replace(lijst, old, new):
	for i in range(len(lijst)):
		if lijst[i] == old:
			lijst[i]=new
	return lijst

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
		while len(argumenten)>0:
			self.body = replace(self.body, self.pram.pop(0), argumenten.pop(0))
		'''for i in range(len(self.body)):
			if len(self.body[i]>1):'''

		return self.body

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

functie_2=str_to_func("(lax.x)")
functie_3=str_to_func("lax.x")
print(functie_2)
print(functie_3)

functie = functie(pram=["a", "b", "c"],body=["a", "b", "c"])
print(functie)
print(functie.beta_redu(["(lb.xy)", "(lsz.z)", "z"]))


