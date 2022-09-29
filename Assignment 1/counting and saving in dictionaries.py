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
print("Counts of alphabets are:")    
print(count_char)    

## Finding out if letter input by a user is in a word

word='ALONGstringHere'
letter=str(input("Enter letter to check : "))

if letter in word:
    print(f"Letter '{letter}' was found in word '{word}'")
else:
    print("Sorry No Luck")

''' You do not need to count white space, other easier approach could be used to perform same task do search them (i.e do not use Counter method) '''
