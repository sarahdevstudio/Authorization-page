#Username and password authorization

startOver = 'Y'

usernameList = []
passwordList = []

# welcomo
#1: login
#2: signup
#3: list of user
print('Welcome to the My application')

while(startOver == 'Y'):
    
    options = input('Chose one of the numbers: 1.Sign up, 2.Login 3.Show the List of User: ')

    if options == '1':
        
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
            
    elif options == '2':
        print('todo') 
        
    elif options == '3':
        
        # user : pass 
        for i in range(len(usernameList)):  
            print(f'{usernameList[i]} : {passwordList[i]}')   
        
        
    else:
        print('your answer is invalid')   

    startOver = input('do you want to go back to menu?(Y/N): ') 