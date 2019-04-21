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
					print(f" {a} a greatest \n")
				else:
					print(f" {e} e greatest \n ")

			elif d>e:
				print(f" {d} d value is greater \n")
			else:
				print(f" {e} e greatest")

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