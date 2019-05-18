c =input("Enter the string : ")
b=input("Letter : ")

def split(c):
	a=[]
	for i in range(len(c)):
		a.extend(c[i])
	print(a)

def string_count(c,b):
	# a = []
	split(c)

	e = c.count(b)

	print(e)

	
string_count(c,b)