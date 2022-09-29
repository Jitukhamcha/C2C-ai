letter = input("Enter a word:")
#print("Your word is ")
#print(a)
#letter.lower()
ourdict = {}
#type(ourdict)
for i in letter:
    if i in ourdict:
        ourdict[i] += 1
    else:
        ourdict[i] = 1
        
print("Frequency of alphabets repetation in given string is: ", ourdict)
