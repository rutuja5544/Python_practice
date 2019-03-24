a=int(input("a : Enter any value:"))
b=int(input("b : Enter any value:"))
c=int(input("c : Enter any value:"))


if a>b:
	if b>c:
		print("b value greater")
	else:
		print("c value is greater")
elif a>c:
	print("a value is greater")

else:
	print("c value is greater")
