#Print multiplication table of given number using for loop
print('Enter the Number whose muliplication table is to be displayed')
number = int(input())
table_range = list(range(1,11))#If I use range(11) then the list will be from 0 to 10 where we dont want 0 so kept two arguments  
#this line 4 can be replace by table_range = [1,2,3,4,5,6,7,8,9,10] which is a simple list

#loop section
for n in table_range : #the values of n changes from 1 to 10 ,for eg: n= 1 in iteration 1 and n=2 in interation 2 and loops 
                       #continues until the list completes also the right side range argument is excluded from list  i.e range is from 1 to 10 as already said
    print(number , ' x ', n , ' = ', number * n, '\n')
