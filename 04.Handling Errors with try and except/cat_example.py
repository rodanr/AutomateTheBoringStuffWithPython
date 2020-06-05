print('How many cats do you have ?')
# We cannot convert it into int cuz we get value error when input is not a numer and get value error in this
# line and program interrups in line 4 also valueerror needs to be find inside the try block
numCats = input() 
try :
    if int(numCats) >= 4 :
        print('That is a lot of cats.')

    else :
        print('That is not a lot of cats.')

except ValueError :
    print('Please give input in integer')