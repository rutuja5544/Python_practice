import random
print("Player 1:")
p1=input().lower()
print("********NO CHEATING******\n\n"*10)
print("Player 2:")
p2=input().lower()

a=random.randint(1,2)

while p1!="quit":
	if p1:
			if p2:
				if p1==p2:
					print("It's a tie")
				
				# Rock
				elif p1=="rock":
					if p2=="paper":
						print("player 2 , PAPER wins..")
					elif p2=="scissor":
						print("Player1 , ROCK wins..")
					else:
						print("Invalid input")	
			

				#Paper
				elif p1=="paper":
					if p2=="scissor":
						print("player 2 , Scissor wins..")
					elif p2=="rock":
						print("Player 1 , PAPER wins..")
					else:
						print("Invalid input")


				#Scissor
				elif p1=="scissor":
					if p2=="paper":
						print("player 1 , Scissor wins..")
					elif p2=="rock":
						print("Player 2 , ROCK wins..")
					else:
						print("Invalid input")

				

				else:
					print("Invalid input, Please Try Again...")

			else:
				print("Player 2 , Enter valid input...")

	else:
		print("Players, Enter valid input..")		
print("quit from palyer 1 	")