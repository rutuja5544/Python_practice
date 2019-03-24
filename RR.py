import random
a = random.random()


p1 = input("Player 1 chance: \n").lower()
p2 = input("Player 2 chance: \n").lower()


if a<0.5:
	c = "tails"
	print("\ntails\n")
elif a>0.5:
	c = "heads"
	print("\nheads\n")

if p1:
	if p2:

		if p1==p2==c:
			print("Both players win. ")
		elif p1==p2!=c:
			print("Both players lose...")	

		elif p1==c:
			print("player 1 wins.")

		elif p2==c:
			print("player 2 wins..") 	

		else:
			print("Enter valid input")	


	else:
		print("player 2 enter something")

else:
	print("players enter something ")






# if b=="heads" and a<0.5:
# 	print(" player 2  wins..")

# elif b=="tails" and a>0.5:
# 	print("tails wins...")


