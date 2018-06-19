from Class_Lambda import functie

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
		
def str_to_expr(tekst):
	return expr1_to_expr(str_to_expr1(tekst),[])

expr = str_to_expr("(labc.a(bc))((lsz.s(sz))(lxy.x(x(xy))))")
print(expr[0].body)