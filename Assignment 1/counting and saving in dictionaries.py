#string
line='My name is Bibek Thapa. I am CSIT student. My favourite animal is Zebra. Currently coding in python.'
#dict for  alphabets
char_count={}
for i in range(0,26):
    char_count[chr(i+96)]=0 #ascii for lower aplhabets set as keys
#now to count
for ch in line.lower():
    if(ch in char_count):
        char_count[ch]+=1

print(char_count)
