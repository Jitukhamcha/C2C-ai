def TOH(n , source, auxiliary, destination):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TOH(n-1, source, destination, auxiliary)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TOH(n-1,auxiliary, source, destination )

TOH(3,'A','B','C')
