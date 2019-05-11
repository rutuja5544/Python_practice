# Comparing in 5 NOs.


a=int(input(" a : value\n"))
b=int(input(" b : value\n"))
c=int(input(" c : value\n"))
d=int(input(" d : value\n"))
e=int(input(" e : value\n"))


if a!=b!=c!=d!=e:
	if a>b:
		if b>c:
			if c>d:
				if d>e:
					print(" d value is greater \n")

				else:
					print(" e value is greater \n")
			elif c>e:
				print(" c value is greater \n")

			elif c>a:
				print(" c value is greater \n")

			else:
				print(" a value is greater \n")

		elif b>d:
			print("b value is greater \n")

		elif b>e:
			print(" b value is greater \n")

		else:
			print(" e value is greater \n")

	elif a>c:
		print(" a value is greater \n")

	elif a>d:
		print(" a value is greater \n")

	elif a>e:
		print(" e value is greater \n")

	else:
		print("e value is greater \n")	

else:
	print(" Same value !!!!!! ")
