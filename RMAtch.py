# Enter any No , and checked that no is same or greater or lower  


import random
a = random.randint(1,10)


b=int(input("\nEnter any no between 1 to 10 :\n\n\n"))



if a==b:
	print("\nNos are same..\n")

elif a<b:
	print("\nits a greater no ... \n")

elif a>b:
	print("\nits a lower no")

else:
	print("\nEnter no .")


print(a)	
