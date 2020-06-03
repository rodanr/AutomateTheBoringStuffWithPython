#Making a program that asks name and age
print ('Hello World !')
print ('What is your name ?')#Asks for the name
name = input()#takes name input
print('Good to meet you '+name)
print('Your name length is ',(int)(len(name)))
print ('What is your age ?')#Asks for the age
age = input()#takes age input
print('Your age will be '+str((int(age)+1))+' after one year')

"""
I learned nothing new in this day but I reviewed the things I know already.

Things done in this day
Asked for Input From Used
Used the console out commands i.e print
Done string concatenation in line no. 9 
Made single line comment using # as seen in the line no. 1,3,7,8
[Note:
While doing string concatenation I got error that int_type and string_type
cannot be concatenated so I converted the integer using str() function which
is prebuilt within python example can be seen in my code line no. 9 
code part :'+str((int(age)+1))'
]
"""

