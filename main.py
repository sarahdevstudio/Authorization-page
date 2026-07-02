#Username and password authorization

usernameList = ['sarah', 'amir', 'sogol']
passwordList = ['123', '456', '789']
#welcomo
#1: sign up
#2: login
#3: list of user
print('\t\t\t\t\tWelcome To My Application')

while(True):
    
    print('-'*100)
    options = input('1.Sign up\n2.Login \n3.Show the List of User\n4.Exit\nChose one of the numbers:')
    
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
                        
                        isChangePassword = input('would you like to change the password?(Y/N): ')
                        
                        if isChangePassword == 'N':
                            break
                        else:
                            newPassword =  input('please enter the new password: ')
                            
                            passwordList[indexUser] = newPassword
                            
                            # passwordList.remove(loginPassword)
                            # passwordList.insert(indexUser,newPassword)
                            
                    else:
                        print('Pasword is invalid! Please try again.')
                
                else:
                    print('Username not found! Please try again!')
                                        
        case '3':
            # user : pass 
            for i in range(len(usernameList)):  
                print(f'{usernameList[i]} : {passwordList[i]}')  
             
        case '4':
            #exit
            break        
            
        case _:
            print('your answer is invalid')   