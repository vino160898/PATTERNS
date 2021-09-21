for row in range(6):
	for col in range(row):
		print(" ",end= " ")
	for col in range(5-row):
		print(col+1,end=" ")
	print()
