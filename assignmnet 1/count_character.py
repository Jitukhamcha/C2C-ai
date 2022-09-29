<<<<<<< HEAD
# initalizing string
string="this is first assignment"
all_char={} #creating dictionary
#creating condition
for i in string:
	if i!= ' ' and i in all_char: # doesn't count space
		all_char[i]+=1
	else:
		all_char[i]=1
#printing result
print('count', str(all_char))
=======
from collections import Counter
string = 'this is the first assignment'
repeated= Counter(string)
print(repeated)
''' Do not use Counter function to count the repetetion of characters in string. 
Search other approaches '''
>>>>>>> 891d6731224249a0fc2015cbd5976f085c7765bd
