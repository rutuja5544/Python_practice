print("Player 1:")
p1=input().lower()
print("********NO CHEATING******\n\n"*100)
print("Player 2:")
p2=input().lower()

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
		# Rock
 		# if p1=="rock" and p2=="paper":
		# 	print("Player 2 Wins...")
		# elif p1=="rock" and p2=="scissor":
		# 	print("Player 1 wins..")

		#Paper
		elif p1=="paper":
			if p2=="scissor":
				print("player 2 , Scissor wins..")
			elif p2=="rock":
				print("Player 1 , PAPER wins..")
			else:
				print("Invalid input")

		#paper		
		# if p1=="paper" and p2=="rock":
		# 	print("Paper Win..")
		# elif p1=="paper" and p2=="scissor":
		# 	print("Scissor win..")

		#Scissor
		elif p1=="scissor":
			if p2=="paper":
				print("player 1 , Scissor wins..")
			elif p2=="rock":
				print("Player 2 , ROCK wins..")
			else:
				print("Invalid input")

		#Scissor		
		# if p1=="scissor" and p2=="rock":
		# 	print("Rock Win..")
		# elif p1=="scissor" and p2=="paper":
		# 	print("Scissor win..")

		else:
			print("Invalid input, Please Try Again...")

	else:
		print("Player 2 , Enter valid input...")

else:
	print("Players, Enter valid input..")		
