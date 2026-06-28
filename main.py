#Username and password authorization

startOver = 'Y'

usernameList = ['sarah', 'amir', 'sogol']
passwordList = ['123', '456', '789']

# welcomo
#1: sign up
#2: login
#3: list of user
print('Welcome to My application')

while(startOver == 'Y'):
    
    options = input('Chose one of the numbers: 1.Sign up, 2.Login 3.Show the List of User: ')
    
    match options:
        case '1':  

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
                
        case '2':
            for x in range(3):

                loginUser = input('Username: ')
                loginPassword = input('Password: ')
                
                if loginUser in usernameList:
                    indexUser = usernameList.index(loginUser)
                    
                    if passwordList[indexUser] == loginPassword:
                        print('successful!')
                        break;
                    else:
                        print('Pasword is invalid! Please try again.')
                
                else:
                    print('Username not found! Please try again!')
                                        
        case '3':
            
            # user : pass 
            for i in range(len(usernameList)):  
                print(f'{usernameList[i]} : {passwordList[i]}')   
            
        case _:
            print('your answer is invalid')   

    startOver = input('do you want to go back to menu?(Y/N): ')     