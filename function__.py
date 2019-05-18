# Prime No  

def prime(a):
	for i in range(2,a):
		if a%i==0:
			print("NOtprime")

			break

		else:
			if i>=a-1:
				print(" Prime no")

prime(88)


