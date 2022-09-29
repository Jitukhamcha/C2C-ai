def is_triangle (a,b,c):
    if ((a+b>c) and (b+c>a) and (a+c>b)):
        print("Yes!, these lenght of stick do make an triangle.")
    else:
        print("No!, these lenght of stick do not make a triangle.")
is_triangle(1,2,3)
is_triangle(3,4,5)
is_triangle(222,333,555)