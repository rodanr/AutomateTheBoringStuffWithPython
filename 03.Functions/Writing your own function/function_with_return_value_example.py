def hi(user_input): # This function returns hello if the user types in hello
    if user_input.lower() == 'hello':
        return('Hi')

print('Type hello to display hi\n')
user_input = input() # The variable user_input here and in function hi(user_input) is different as user_input is
#                    # unknown outside the hi(user_input) fucntion
print(hi(user_input))