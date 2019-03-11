P1= input()
P2= input()
if P1=="rock" and P2=="paper":
	print("Player 2 Wins...")
elif P1=="rock" and P2=="scissor":
	print("Player 1 wins..")
elif P1=="rock" and P2=="rock":
	print("It's a tie..!!")
elif P1=="paper" and P2=="rock":
	print("Paper Win..")
elif P1=="paper" and P2=="scissor":
	print("Scissor win..")
elif P1=="paper" and P2=="paper":
	print("It's a tie..!!")
elif P1=="scissor" and P2=="rock":
	print("Rock Win..")
elif P1=="scissor" and P2=="paper":
	print("Scissor win..")
elif P1=="scissor" and P2=="scissor":
	print("It's a tie..!!")
