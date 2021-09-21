for row in range(6,0,-1):
	for col in range(row):
		print(" ",end=" ")
	print("  * "*(5-row+1),end=" ")
	print()
