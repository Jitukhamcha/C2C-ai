from itertools import count


#question no. 3 of set B, by Srijan Aryal, BE-Cmp, EEC
str = input("Enter a string")
print(str)
print(type(str))
char = 0
for x in str:
    char = char + 1
    #print (char)
print ("Total no. of characaters in given string =", char)