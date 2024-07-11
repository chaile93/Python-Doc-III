#!/usr/bin/env python
# coding: utf-8

# # Data Collections 2 (Dictionaries, Sets) and Importing Modules

# ## Tasks Today:
# 
# 1) Dictionary <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring (key, value) <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accessing Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #1 - Print the eye color of each person in a double nested dict <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Adding New Pairs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Modifying Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Removing Key, Value Pairs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Looping a Dictionary <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Looping Only Keys <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Looping Only Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format()  <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) sorted() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Lists with Dictionaries <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; k) Dictionaries with Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; l) Dictionaries with Dictionaries <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; ------ Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, which prints all names and addresses after they're done putting information in...  <br>
# 2) Dictionaries vs. Lists (over time)<br>
# 3) Set <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) .add() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .union() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .intersection() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .difference() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Frozen Set <br>
# 4) Modules <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Importing Entire Modules <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Importing Methods Only <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Using the 'as' Keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Creating a Module <br>
# 5) Exercises <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Build a Shopping Cart <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Create Your Own Module <br>

# ## Dictionary <br>
# <p>A collection of data with 'key:value' pairs. Dictionaries are ordered as of Python 3.6</p>

# ##### Declaring (key, value)

# In[ ]:





# ##### Accessing Values

# In[ ]:





# ## In-Class Exercise #1 - Print a formatted statement from the dictionary below <br>
# <p>The output should be '2018 Chevrolet Silverado'</p>

# In[1]:


# use the dict below
truck = {
    'year': 2018,
    'make': 'Chevrolet',
    'model': 'Silverado'
}

output = 'year' + 'make' + 'model'
print(output)


# ##### Adding New Pairs

# In[ ]:





# ##### Modifying Values

# In[ ]:





# ##### Removing Key, Value Pairs

# In[ ]:





# ##### Looping a Dictionary

# In[ ]:


# .items()
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)



# ##### Looping Only Keys

# In[ ]:


# .keys()



# ##### Looping Only Values

# In[ ]:


# .values()



# ## In-Class Exercise #2 - Create a Function that Prints All Key Value Pairs within a print .format() <br>
# <p><b>Output should be:</b><br>
# Max has blue eyes<br>
# Lilly has brown eyes<br>
# Barney has blue eyes<br>
# etc.
# </p>

# In[ ]:


# use the dict below

people = {
    'Max': 'blue',
    'Lilly': 'brown',
    'Barney': 'blue',
    'Larney': 'brown',
    'Ted': 'purple'
}


# ##### sorted()

# In[ ]:


# sorts variables in order
# sorted(dict.values()) or dict.keys() or dict.items()



# ##### List with Dictionaries

# In[ ]:





# ##### Dictionaries with Lists

# In[ ]:


# be careful when using numbers as keys in dictionaries, don't confuse them with indexes


# ##### Dictionaries with Dictionaries

# In[ ]:


# to get values, must traverse through keys



# ## Dictionaries vs. Lists (over time) Example of RUNTIME
# ### When inputting values in a Dictionary vs List

# In[ ]:


import time


# generate fake dictionary
d = {}

for i in range(10000000):
    d[i] = 'value'
    

# generate fake list
big_list = [x for x in range(10000000)]


# In[ ]:


# tracking time for dictionary
start_time = time.time()

print(d[9999999])

end_time = time.time() - start_time

print('Elapsed time for dictionary: {}'.format(end_time))


# tracking time for list
start_time = time.time()

for i in range(len(big_list)):
    if i == 9999999:
        print(i)

end_time = time.time() - start_time

print('Elapsed time for list: {}'.format(end_time))


# ## Exercise #3 - Write a Function that asks someone's name and address, and then stores that into a dictionary, and continues to do so until they choose to 'quit'. Once they quit, the program should print all names and addresses. <br>
# <p>
# <b>Proper steps:</b><br>
# step 1: write a function that takes in information and stores it in a dictionary<br>
# step 2: define an empty dictionary to work with<br>
# step 3: create our loop, which asks the user for information until they quit<br>
# step 4: ask for the information, and store it into variables<br>
# step 5: check if the user types quit<br>
# step 5a: print out all information<br>
# step 5b: break out of the loop<br>
# step 6: if they didn't quit, add the information to the dictionary<br>
# step 7: invoke the function by calling it
# </p>

# In[8]:


from IPython.display import clear_output

#step 1
def storeInfo():
    d ={}
#step 2

#step 3
    while true:
#step 4
        name = input("Enter a name to be stored or say 'quit': ")
        address = input("Enter a address to be stored or say 'quit': ")
        clear_output()
#step 5
        if name.lower() == 'quit' or address.lower() == 'quit':
#step 5a
            for key, value in d.items():
                print(f'The address for {key} is {value}')
            break
        d[name] = address
storeInfo()


# ## Set <br>
# <p>A Set is an unordered collection data type that is iterable (loop), mutable, and has no duplicate elements.<br>Major advantage is that it is highly optimized in checking if something is in the set, as opposed to checking if something is in a list.</p>

# ##### Declaring

# In[ ]:


# set() or {}
# no order {3, 2, 1} outputs as {1, 2, 3}


# ##### .add()

# In[ ]:


# set.add()


# ##### .remove()

# In[ ]:


# removes by value
# set.remove()
# nums.remove(56)



# ##### .union() 

# In[ ]:


# Returns a union of two sets, can also use '|' or set.union(set)
# joins all numbers, gets rid of duplicates


# ##### .intersection()

# In[ ]:


# Returns an intersection of two sets, can also use '&'
# only takes similar elements from both sets



# ##### .difference()

# In[ ]:


# Returns a set containing all the elements of invoking set that are not in the second set, can also use '-'
# only takes values from the first set that are not in the second set
# order matters



# ##### .clear()

# In[ ]:


# Empties the whole set
# set.clear()


# ##### Frozenset <br>
# <p>Frozen sets are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.</p><br><b>Unique & Immutable</b>

# In[ ]:


# frozenset([])


# ## Modules

# ##### Importing Entire Modules

# In[ ]:


# import or from 'xxx' import *
# import math



# ##### Importing Methods Only

# In[ ]:


# from 'xxx' import 'xxx'
# from math import floor




# ##### Using the 'as' Keyword

# In[ ]:


# from 'xxx' import 'xxx' as 'xxx' or import 'xxx' as 'xxx'
# from math import floor as f


# ##### Creating a Module

# In[ ]:





# # Exercises

# ### 1) Build a Shopping Cart <br>
# <p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
# 1) Takes in input <br>
# 2) Stores user input into a dictionary or list <br>
# 3) The User can add or delete items <br>
# 4) The User can see current shopping list <br>
# 5) The program Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>
# </p>

# In[13]:


from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def shopping_cart():
    cart = [] 
    
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Delete item")
        print("3. View shopping list")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            item = input("Enter item to add: ").strip()
            cart.append(item)
            print(f"Added '{item}' to your shopping list.")
        
        elif choice == '2':
            if not cart:
                print("Your shopping cart is empty.")
            else:
                print("Your current shopping list:")
                for index, item in enumerate(cart, start=1):
                    print(f"{index}. {item}")
                item_to_delete = int(input("Enter the number of item to delete: ").strip())
                if 1 <= item_to_delete <= len(cart):
                    deleted_item = cart.pop(item_to_delete - 1)
                    print(f"Deleted '{deleted_item}' from your shopping list.")
                else:
                    print("Invalid item number.")
        
        elif choice == '3':
            if not cart:
                print("Your shopping cart is empty.")
            else:
                print("Your current shopping list:")
                for index, item in enumerate(cart, start=1):
                    print(f"{index}. {item}")
        
        elif choice == '4':
            print("Thank you for shopping with us! Here is your final shopping list:")
            for index, item in enumerate(cart, start=1):
                print(f"{index}. {item}")
            break
        
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4).")


# ### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<br>
#         <hr>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

# In[15]:


import module.py

