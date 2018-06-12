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

	def alfa_redu(self):
		pass

	def beta_redu(self, argumenten):
		while len(argumenten)>0:
			self.body = replace(self.body, self.pram.pop(0), argumenten.pop(0))
		'''for i in range(len(self.body)):
			if len(self.body[i]>1):'''

		return self.body

functie = functie(pram=["a", "b", "c"],body=["a", "b", "c"])
print(functie)
print(functie.beta_redu(["(lb.xy)", "(lsz.z)", "z"]))


