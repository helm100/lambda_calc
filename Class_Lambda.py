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
		return [self]

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

def evalueer_2(lijst):
	if isinstance(lijst[0], functie):
			return evalueer(lijst[0].beta_redu(lijst[1:]))
	else:
		return lijst[0]+evalueer(lijst[1:])

functie1 = functie(["y", "x"], ["x"])
functie2 = functie(["y"], ["y"])
functie3 = functie(["a", "b"], [functie2, functie1, "a"])

lijst = [functie1, "a","b", functie3, "c", functie2]

for x in evalueer_2(lijst):
	print(x)


