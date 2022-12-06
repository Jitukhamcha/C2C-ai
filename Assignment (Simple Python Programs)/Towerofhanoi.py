def TowerOfHanoi(n, source, destination, intermediate):
	if(n<1):
		print("Not Possible")
		return
	if(n==1):
		print("Move disk 1 from source", source, "to destination", destination)
		return
	TowerOfHanoi(n-1, source, intermediate, destination)
	print("Move disk {} from {} to {}" .format(n, source, destination))
	TowerOfHanoi(n-1, intermediate, destination, source)
n=4
TowerOfHanoi(n,'A','B','C')

	
