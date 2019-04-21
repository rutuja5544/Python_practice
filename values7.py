a=int(input(" a : value\n"))
b=int(input(" b : value\n"))
c=int(input(" c : value\n"))
d=int(input(" d : value\n"))
e=int(input(" e : value\n"))
f=int(input(" f : value\n"))
g=int(input(" g : value\n"))


if a!=b!=c!=d!=e:
	if a>b:
		if a>c:
			if a>d:
				if a>e:
					if a>f:
						if a>g:
							print(f"{a} a greatest")
						else:
							print(f"{g} g greatest")
					elif f>g:		
					print(f" {f} f greatest \n")
				else:
					print(f" {g} g greatest \n ")

			elif e>f:
				print(f" {e} e value is greater \n")
			
			


		elif c>d:
			print(f" {c} c value is greater \n")

		elif d>e:
			print(f" {d} d value is greater \n")
		else:
			print(f" {e}e greatest")

	elif b>c:
		print(f" {b} b value is greater \n")

	elif c>e:
		print(f" {c}c value is greater \n")
	else:
		print(f"{e}e greatest")

else:
	print(" Same value !!!!!! ")