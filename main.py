#Username and password authorization

startOver = 'Y'

usernameList = ['admin' , 'admin 2']
passwordList = ['123' , '22222']

while(startOver == 'Y'):
    
    username = input('Please create your Username: ')
    password = input('Please Create a password: ')
    password2 = input('Please add your password again: ')

    if password != password2:
        for i in range(3):
            
            print('Please try again!') 
            password2 = input('Please add the password again: ')
            
            if password == password2:
                print('Password created!')
                break

    else:
        ('Password created!')

    if password2 == password:
        usernameList.append(username)
        passwordList.append(password)
            
     # user : pass   
    for item in passwordList:
        print(item)
        
    for user in usernameList:
        print(user)       
    startOver = input('do you want to create another acount?(Y/N): ')

