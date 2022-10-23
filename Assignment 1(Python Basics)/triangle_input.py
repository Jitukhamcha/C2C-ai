print("Can I form a Triangle?")
def is_traingle(sides):
    sides.sort()
    if((sides[2]<sides[0]+sides[1])):
        print(f"You can form the triangle with sides : {sides[0]},{sides[1]},{sides[2]}")
    else:
        print(f"You cannont form the triangle with sides : {sides[0]},{sides[1]},{sides[2]}")

def input_sides():
    sides=[0,0,0]
    for i in range(0,3):
        sides[i]=(int(input(f"Enter {i+1} side of triangle : ")))
        
    #function_call
    is_traingle(sides)    

input_sides()


