#string
line='My name is Bibek Thapa. I am CSIT student. My favourite animal is Zebra. Currently coding in python.'
#alphabet to compare
alphabet=[]
for i in range (0,26):
    alphabet.append(chr(i+97))

#counting character
count_char={}
for ch in line:
    lalp=ch.lower()
    if (lalp in alphabet):
        if (lalp in count_char):
            count_char[lalp]+=1
        else:
            count_char.update({lalp:1})
    
print(count_char)    

