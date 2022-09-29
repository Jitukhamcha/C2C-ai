#code to check if the given length are triangle or not
#basis logic is that the sum of two sides of a triangle is always greater than the third side
#if sum of two sides is euql to the third side it will form a deformed triangle

#funciton declaration
def triangle_check(a,b,c):
    if a+b >c and b+c > a and c+a>b :
        return True
    else:
        return False

def deformed_triangle_check(a,b,c):
    if a+b ==c or b+c ==a or c+a ==b:
        return True
    else:
        return False


#input section
a=float(input("Enter length of side a:"))
b=float(input("Enter length of side b:"))
c=float(input("Enter length of side c:"))


#function call
if triangle_check(a,b,c) :
    print("the sides are of the regular triangle")
else:
    if deformed_triangle_check(a,b,c):
        print("The sides form a deformed triangle")
    else:
        print("The sides doesn't form a triangle")



'''
Apparently it's correct,
Just a suggestion, you can use [list] apporach [just want to see you logic/mathematics]
'''