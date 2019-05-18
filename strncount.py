a=input("Enter the string : ")

def str(a):
	b=[]
	for i in range(len(a)):
		b.extend(a[i])
	print(b)

	for i in range(len(a)):
		r = 0
		for j in range(len(b)):
			if b[i] == b[j]:
				r += 1
		print(f"{b[i]} - {r}")

str(a)

