a=int(input("Enter no:"))
num=a
# prime
for i in range(2,a):

# even or odd
	if num%2==0:
		print("2")
		num=num/2

	elif num%5==0:
		print("5")
		num=num/5

	elif num%3==0:
		print("3")
		num=num/3

	elif num%7==0:
		print("7")
		num=num/7

	elif num == 1:
		break

	else:
		print(f"{num}","1")
		break