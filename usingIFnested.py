a = int(input("\nEnter your marks :"))
if a>35:
	if a >=35 and a<50:
		print("\nsecond class")
	elif a>=50 and a<60:	
		print("\nHigher second")
	elif a>=60 and a<70:
		print("\nfirst class")
	elif a>=70 and a<100:	
		print("\nDistinction")
	else:
		print("\nWrong Input..")
else:
	print("\nFail..")