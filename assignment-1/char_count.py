#count number of each character in the string
#by using dictionary

#funciton declaration

def count_char(string):
    dictionary={} #creating and empty dicitonary
    for keys in string:
        dictionary[keys] = dictionary.get(keys,0) + 1

    return dictionary


#input section
string = str(input('Enter a string:'))

dictionary = count_char(string)

print(dictionary)

'''
Spaces are also count as character. But in this case, try avoiding spaces
'''