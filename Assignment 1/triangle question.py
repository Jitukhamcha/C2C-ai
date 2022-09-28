
print("Can I form a Triangle?")
def is_traingle(sd1,sd2,sd3):
    if((sd1+sd2>sd3)and(sd1+sd3>sd2)and(sd2+sd3>sd1)):
        print(f"You can form the triangle with sides : {sd1},{sd2},{sd3}")
    else:
        print(f"You cannont form the triangle with sides : {sd1},{sd2},{sd3}")

is_traingle(9,3,3)
is_traingle(2,3,3)
        


