#Username and password authorization
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
       