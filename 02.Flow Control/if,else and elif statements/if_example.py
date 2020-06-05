#This Program asks for the sur name if and only if the first name is Ram
print('What is your first name ?')
firstName = input()
if(firstName.lower() == 'ram'):
    print('What is your sur name ?')
    surName = input()
    print('Hello '+firstName+' '+surName)
