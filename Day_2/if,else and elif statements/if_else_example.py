#Checking which is greater number between a and b

#Asking values for a and b
print('Enter value of a')
#If we donot convert it into the integer type then string is compared rather than number and causes error
a = int(input())
print('Enter value of b')
b = int(input())

#Comparison using if,else 
if a>b :
    print('a is greater than b')

else :
    print('b is greater than a')

