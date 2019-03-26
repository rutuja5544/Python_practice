a=int(input("a value:\n\n"))
b=int(input("b value:\n\n"))
c=int(input("c value:\n\n"))
d=int(input("d value:\n\n"))

if a>b:
	if b>c:
		if c>d:
			print(" c value value is greater")

		else:
			print(" d value value is greater")

	elif b>d:
		print("b value value is greater")

	else:
		print(" d value is greater")

elif a>c:
	print(" a value value is greater")

elif a>d:
	print(" a value is greater")

else:
	print(" d value is greater")

