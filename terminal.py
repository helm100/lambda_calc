from str_to_expr import str_to_expr

#welke invoer is wel geldig en welke niet

input_user=""
while input_user != "exit":
	input_user = input()
	print(input_user)
	lambda_versie_input = str_to_expr(input_user)
	print(lambda_versie_input)
	'''
	gereduceerde_lambda_versie = ...
	print(gereduceerde_lambda_versie)
	uitkomst = ...
	print(uitkomst)
	'''
print("Thank you for using me!")


