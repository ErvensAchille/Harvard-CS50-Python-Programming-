from functions import square 

for i in range (10):
     print (f"the square root of {i} is {square(i)}")

import functions
for i in range (10):
     print (f"the square root of {i} is {functions.square(i)}")

# in order to use a function from another file you need to import it in
# example 1: from the functions.py python module import square 
# function to be used

# example 2: import the entire module with dot notation ex: {functions.square(i)}

# this works for built in modules from python or others to access features