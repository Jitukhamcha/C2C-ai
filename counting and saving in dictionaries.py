#string
line='My name is Bibek Thapa. I am CSIT student. My favourite animal is Zebra. Currently coding in python.'
#alphabet to compare
alphabet=[]
for i in range (0,26):
    alphabet.append(chr(i+97))

#counting character
count_char={}
for ch in line:
    alp=ch.lower()
    if (alp in alphabet):
        if (alp in count_char):
            count_char[alp]+=1
        else:
            count_char.update({alp:1})
    
print (count_char)
    

