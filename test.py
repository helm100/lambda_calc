usr_inp = ""

def numb_to_lamb(numberstr):
	n = int(numberstr)
	l_str = "(lsz."
	for i in range(n):
		l_str += "s("
	l_str += "z"+")"*(n+1)
	print(l_str)
	
while usr_inp != "exit":
	usr_inp = input()
	numb_to_lamb(usr_inp)