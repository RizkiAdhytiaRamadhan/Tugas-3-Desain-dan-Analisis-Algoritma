#!/usr/bin/env python
# coding: utf-8

# # Struktur Data

# ## 1.    Lists
# ## 1.1 Lists

# In[1]:


aList = ["John", 33,"Toronto", True]


# In[2]:


aList


# In[3]:


type(aList)


# In[4]:


bin_colors=['Red','Green','Blue','Yellow']


# # 2.   Tuples
# ## Tuples

# In[5]:


bin_colors=('Red','Green','Blue','Yellow')
print(f"The second element of the tuple is {bin_colors[1]}")


# In[7]:


print(f"The third element of the tuple is {bin_colors[2:]}")


# In[8]:


nested_tuple = (1,2,(100,200,300),6)
print(f"The maximum value of the inner tuple is {max(nested_tuple[2])}")


# # Dictionary
# ## 1.2 Dictionary

# In[9]:


bin_colors ={
    "manual_color": "Yellow",
    "approved_color": "Green",
    "refused_color": "Red"
}


# In[10]:


print(bin_colors)


# In[11]:


bin_colors.get('approved_color')


# In[12]:


bin_colors['approved_color']


# In[13]:


bin_colors['approved_color']="Purple"


# In[14]:


print(bin_colors)


# # 4. Sets
# ## 1.3 Set

# In[15]:


green = {'grass', 'leave'}
print(green)


# In[16]:


yellow = {'dandelions', 'fire hydrant', 'leaves'}
red = {'fire hydrant', 'blood', 'rose', 'leaves'}


# In[17]:


print(f"The union of yellow and red sets is {yellow|red}")


# In[18]:


print(f"The intersaction of yellow and red is {yellow&red}")


# # DataFrames
# # 1.4 DataFrame

# In[19]:


import pandas as pd
df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]])
df.columns = ['id', 'name', 'age', 'decision']
print(df)


# ## 1.4.1 Column Selection

# In[20]:


df[['name', 'age']]


# the positioning of a column is deterministic in a data frame. Fourth column can be retrieved by its position as fellows

# In[21]:


df.iloc[:,3]


# ## 1.4.2 Row Selection

# In[22]:


df.iloc[1:4,:]


# In[23]:


df[df.age>30]


# # Matrix
# ## 1.5 Matrix

# In[24]:


import numpy as np
myMatrix = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])


# In[25]:


print(myMatrix)


# In[26]:


print(type(myMatrix))


# In[27]:


myMatrix.transpose()


# # II. Tipe Data Abstrak
# #     1.   Vector

# # Vector

# In[28]:


myVector = [ 22,33,44,55]
print(myVector)


# In[29]:


print(type(myVector))


# In[30]:


myVector = np.array([22,33,44,55])
print(myVector)


# In[31]:


print(type(myVector))


# ## 2. Stack
# # 2 Stack

# In[32]:


class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
        


# In[33]:


stack=Stack()
stack.push('Red')
stack.push('Green')
stack.push('Blue')
stack.push('Yellow')


# ## Pop

# In[34]:


stack.pop()


# In[35]:


stack.isEmpty()


# In[36]:


colors = ['Red']


# In[37]:


colors.append('Green')
colors.append('Yellow')
colors.append('Blue')


# In[38]:


colors


# # 3. Queue
# ## Queue

# In[55]:


class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()    
    def size(self):
        return len(self.items)


# In[56]:


queue = Queue()


# In[57]:


queue.enqueue("Red")


# In[58]:


queue.enqueue("Green")


# In[59]:


queue.enqueue("Blue")


# In[60]:


queue.enqueue("Yellow")


# In[61]:


print(f"size of queue is {queue.size()}")


# In[62]:


print(queue.dequeue())


# In[ ]:




