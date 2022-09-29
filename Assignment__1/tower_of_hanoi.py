def toh(n,s,d,a): #s=source,d=destination,a=axiallly(helper)
    if n>0:
        if n==1:
            print("Transfer disk",n, "from",s,"to",d)
            return
        toh(n-1,s,a,d)
        print("Transfer disk",n,"from",s,"to",d)
        toh(n-1,a,d,s)
    else:
        print("Invalid input!!")

n = int(input("Enter the no of disc"))
toh(n,'A','B','C')