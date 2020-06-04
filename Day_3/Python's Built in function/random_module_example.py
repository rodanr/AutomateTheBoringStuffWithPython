import random # Importing random module 
# This is the example of the random module which is an standard python library
# This module helps to generate random number between an intervals of the number
print(random.randint(1,6))# This line displays the random integer value between 1 and 6 i.e {1,2,3,4,5,6}

"""
NOTE :
The import of module can be done in another way also
as the line 1 above can be replaced by "from random import *" 
where the * means everything with any extensions
Similary using this import we don't have to use the . operator and the module name to call the function 
everytime.
Instead the function can be called directly For Example: Line 4 can be replaced by "print(randint(1,6))"
"""