# In[1]:


print('hello')


# In[2]:


inputstring=input('enter a sting')


# In[3]:


print('input string is:',inputstring)


# In[7]:


def towerOfHannoi(n,source,destination,auxiliary):
    if n==1:
        print("move disk 1 from source",source,"to destination",destination)
        return
    towerOfHannoi(n-1,source,auxiliary,destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    towerOfHannoi(n-1,auxiliary,destination,source)
    n=4
    towerOfHannoi(n,'A','B','C')


# In[6]:


print('hi')


# In[8]:


def towerOfHannoi(n,source,destination,auxiliary):
    if(n==1):
        print("move disk 1 from source",source,"to destination",destination)
        return


# In[11]:


def towerOfHannoi(n,source,destination,auxiliary):
    if(n==1):
        print("move disk 1 from source",source,"to destination",destination)
        return
towerOfHannoi(n-1, source,auxiliary,destination)
print("Move disk",n,"from source",source,"to destination",destination)
towerOfHannoi(n-1,auxiliary,destination,source)
n=4
towerOfHannoi(n,'A','B','C')


# In[10]:


def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         

n = 4
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods


# In[13]:


def is_triangle(length_1,length_2,length_3):
    if length_1+length_2>length_3 or length_1+length_3>length_2 or length_2+length_3>length_1:
    return ('yes triangle can be formed')
else:
    return ('no triangle cannot be formed')

is_triangle(12,1,1)


# In[14]:


def is_triangle(length_1,length_2,length_3):
    if length_1+length_2>length_3 or length_1+length_3>length_2 or length_2+length_3>length_1:
        return ('yes triangle can be formed')
else:
    return ('no triangle cannot be formed')

is_triangle(12,1,1)


# In[15]:


def is_triangle(length_1,length_2,length_3):
    if length_1+length_2>length_3 or length_1+length_3>length_2 or length_2+length_3>length_1:
        return ('yes triangle can be formed')
    else:
        return ('no triangle cannot be formed')

is_triangle(12,1,1)


# In[30]:


def is_triangle(length_1,length_2,length_3):
    if length_1+length_2<length_3 or length_1+length_3<length_2 or length_2+length_3<length_1:
        return ('no triangle can be formed')
    else:
        return ('yes triangle cannot be formed')

is_triangle(12,1,1)


# In[18]:


def is_triangle(length_1,length_2,length_3):
    if length_1+length_2<length_3 or length_1+length_3<length_2 or length_2+length_3<length_1:
        return False
    else:
        return True
    length_1=(input('enter lenght of stick 1:'))
    length_2=(input('enter length of stick 2:'))
    length_3=(input('enter length of stick 3:'))


# In[19]:


def is_triangle(length_1,length_2,length_3):
    if length_1+length_2<length_3 or length_1+length_3<length_2 or length_2+length_3<length_1:
        return False
    else:
        return True


# In[20]:


length_1=(input('enter lenght of stick 1:'))
length_2=(input('enter length of stick 2:'))
length_3=(input('enter length of stick 3:'))


# In[23]:


if is_triangle(length_1,length_2,length_3):
    print('yes triangle can be formed')
else:
    print('no triangle cannot be formed')


# In[24]:


my_string=input("enter string:")


# In[25]:


if "e" in my_string:
    print('yes the letter is present')
else:
    print('no the letter is not present')


# In[27]:


if "z" in my_string:
    print('yes the letter is present in string')
else:
    print('no the letter is not present in string')


# In[ ]:




'''

If you are using jupyter notebook for code, then save file in .ipynb format not in .py 

'''