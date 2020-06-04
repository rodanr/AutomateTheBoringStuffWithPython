a = 2 # Global Scope Variable that is applicable and effects the whole code

def test():
    a =3 # Local Scope Variable that means this variable effect and applicablity limits to the function only
    print(a)

test() # Displays a from test() function
print(a) # Displays a from the global scope

"""
NOTE:
1.Code in the global scope cannot use any local variables
2.Code in a local scope can access global variable
3.Code in one function's local scope cannot use variable in another local scope
4.Name of the local scope of one function can use the same name in another local scope
5.Interpreter first search the variable inside the local scope and if doesn't find then only searches in global scope
"""