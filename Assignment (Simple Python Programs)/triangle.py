def is_triangle(x,y,z):
    if x+y>=z and y+z>=x and z+x>=y:
        return True
    else:
        return False

sidex = float(input("Enter length of side x= "))
sidey = float(input("Enter length of side y= "))
sidez = float(input("Enter length of side z= "))


if is_triangle(sidex, sidey, sidez):
    print("Yes it is a triangle")
else:
    print("No it is not a triangle")