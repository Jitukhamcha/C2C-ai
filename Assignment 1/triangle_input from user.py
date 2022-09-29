def is_triangle (a,b,c):
    if a+b==c or b+c==a or a+c==b:
        print("Yes!, these lenght of stick do make an triangle.")
    else:
        print("No!, these lenght of stick do not make a triangle.")

def inp():
    global x,y,z
    x = int(input("Enter the lenght of first stick:"))
    y = int(input("Enter the lenght of second stick:"))
    z = int(input("Enter the lenght of third stick:"))
inp()
#print(x)
#print(y + z)
is_triangle (x,y,z)
    