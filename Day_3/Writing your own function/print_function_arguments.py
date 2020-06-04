# Print function adds up new line at the end of it as the hello and world gets separated by new line
print('Hello')
print('World!')
print('------------------------------------------------')
# Now replacing the print's function default argument to single comma or anything we want at the end 
print('Hello',end=',')
print('World!')

#Look this function
print('Hi','Bye','Tata') # A single space is kept by default by the print function 
print('------------------------------------------------')
print('Hi','Bye','Tata',sep='-') # Single space is replaced by '-' now