import random
a = random.randint(0,2)

# 0 -> rock
# 1 -> paper
# 2 -> scissors

b = input("Player's chance: \n")

if b:
	print("Invalid..")



if a == 0:
	print("Computer: Rock")
elif a ==1:
	print("Computer: Paper")
elif a ==2:
	print("Computer: Scissors")

if a == 0 and b == "rock":
	print("It's a tie..")

elif a == 0 and b == "paper":
	print("Player wins..!!")

elif a == 0 and b == "scissors":
	print("Computer Wins")

if a == 1 and b == "paper":
	print("It's a tie..")

elif a == 1 and b == "scissors":
	print("Player wins..!!")

elif a == 1 and b == "rock":
	print("Computer Wins")	

if a == 2 and b == "scissors":
	print("It's a tie..")

elif a == 2 and b == "rock":
	print("Player wins..!!")

elif a == 2 and b == "paper":
	print("Computer Wins")
