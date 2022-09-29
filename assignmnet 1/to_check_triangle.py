def is_triangle(stick1, stick2, stick3):
    if stick1+stick2<stick3 or stick3+stick2<stick1 or stick1+stick3<stick2:
        print ('no cannot form a triangle')
    else:
        print ('yes can form a triangle')

is_triangle(12,1,1)