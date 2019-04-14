import random				
a=int(input("Enter No:"))

r=random.randint(1,11)
b=2


for i in range(1,4):
	if r==a:
		print("guess is correct")
		
	# elif r<a:
	# 	print("guess no is greater")
	
	# elif r>a:
	# 	print("guess no is lower")

		b=b-1
		break

	else:
		print(f" try again {b}  ")
		b=b-1

	a=int(input("enter no again:"))		

	if b==0:
		break

print(f"your chances are over , correct value is {r}")