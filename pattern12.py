no=1
for row in range(6,0,-1):
	for col in range(row-1):
		print(no,end="  ")
	print(end="*  "*no)
	print()
	no+=1
