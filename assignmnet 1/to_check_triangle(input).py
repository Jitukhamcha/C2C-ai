def is_triangle(stick1, stick2, stick3):
    if stick1+stick2<stick3 or stick3+stick2<stick1 or stick1+stick3<stick2:
        return False
    else:
        return True

stick1=(input('enter length of stick1:'))
stick2=(input('enter length of stick2:'))
stick3=(input('enter length of stick3:'))
if  is_triangle(stick1, stick2, stick3):
    print('yes can form a triangle')
else:
    print('no cannot form a triangle')
'''If possible explain your logic in the form of comment'''
