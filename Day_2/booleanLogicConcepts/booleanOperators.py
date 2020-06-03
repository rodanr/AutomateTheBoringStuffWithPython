#We are discussing the basic boolean operators here that is and ,or ,not

#1.and
"""
The outcome can be explained by the table below
Consider the variable expression to be A and B where the Boolean data type is only considered of the A , B variable

TABLE:
......................
A       B       RESULT
......................
False   False   False
False   True    False
True    False   False
True    True    True
......................

Examples:
"""
#This example justifies the conditon no. 4th of the table i.e for True outcome
print("Boolean data type of 42<43 and 50>40 is ",42<43 and 50>40)
#This example justifies the conditon no. 3rd of the table i.e for False outcome
print("Boolean data type of 42<43 and 50<40 is ",42<43 and 50<40)

#2.or
"""
The outcome can be explained by the table below
Consider the variable expression to be A or B where the Boolean data type is only considered of the A , B variable

TABLE:
......................
A       B       RESULT
......................
False   False   False
False   True    True
True    False   True
True    True    True
......................

Examples:
"""
#This example justifies the conditon no. 4th of the table i.e for True outcome
print("Boolean data type of 42<43 and 50>40 is ",42<43 or 50>40)
#This example justifies the conditon no. 3rd of the table i.e for True outcome
print("Boolean data type of 42<43 and 50<40 is ",42<43 or 50<40)


#3.not
"""
not complements the boolean data type that if the expression if true then using not on it makes is false
Example:
"""
#This displays 42>43 is false
print('The Boolean data type of 42>43 without using not is ',42>43)
#After using the not in it complements the result
print('The Boolean data type of 42>43 using not is ', not 42>43)


