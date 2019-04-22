# Print NO Pattern = 1234
# 		     123
# 		     12
# 		     1
			
for i in range(4,0,-1):
	for a in range(1,i+1):
		print(f"{a}",end=" ")	
	print(end =" \n")
