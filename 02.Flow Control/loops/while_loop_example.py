#reverse the number using while loop
#Taking input of the number
print('Enter a Number to reverse')
number = int(input())
backupNumber = number
reversedNumber = 0
while number>0 :
    rem = number % 10
    reversedNumber = reversedNumber * 10 + rem
    number = int(number /10)

print('The Reverse of ',backupNumber,' is ',reversedNumber)
