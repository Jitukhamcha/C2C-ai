#code to check if the given length are triangle or not
#basis logic is that the sum of two sides of a triangle is always greater than the third side


#funciton declaration
def triangle_check(a,b,c):
    if a+b >c and b+c > a and c+a>b :
        return True
    else:
        return False

#input section
a=float(input("Enter length of side a:"))
b=float(input("Enter length of side b:"))
c=float(input("Enter length of side c:"))


#function call
if triangle_check(a,b,c) :
    print("the sides are of the triangle")
else:
    print(("The sides doesn't form a triangle"))



