print("What to do for today ? ")

l=[]
c = " " 

while c !="q":
	c = input()
	l.append(c)

l.pop()
print("\n")
for i in range(0,len(l)):
	print(f"{i+1}. {l[i]}")