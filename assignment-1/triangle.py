#code to check if the given length are triangle or not
#basis logic is that the sum of two sides of a triangle is always greater than the third side
#if sum of two sides is euql to the third side it will form a deformed triangle

#funciton declaration
def triangle_check(x):
    #sorting the list for easier comparision
    x.sort()
    if x[2] < x[1] + x[0] :
        return True
    else:
        return False

def deformed_triangle_check(x):
    if x[2]  == x[1] +x[0] :
        return True
    else:
        return False


#input section
a=float(input("Enter length of side a:"))
b=float(input("Enter length of side b:"))
c=float(input("Enter length of side c:"))

#creating a list with sides of triangle
x = [a,b,c]


#function call
if triangle_check(x) :
    print("the sides are of the regular triangle")
else:
    if deformed_triangle_check(x):
        print("The sides form a deformed triangle")
    else:
        print("The sides doesn't form a triangle")



'''
Apparently it's correct,
Just a suggestion, you can use [list] apporach [just want to see you logic/mathematics]
'''