pwd = input('What is the master password? ')

def addpw():
    pass

def viewpw():
    pass

def deletepw():
    pass

while True:
    print('--------------------------------')
    print("Welcome to Password Manager! \n Please select an option:")
    print("1. Add new password")
    print("2. View existing password(s)")
    print("3. Modify existing password(s)")
    print("4. Delete a password")
    print("5. Exit")
    mode = input('Select a mode(1-5): ')

    #
    #  All the modes to access and modify the passwords in password manager
    #  Options:  1 = add, 2 = view, 3 = modify, 4 = delete, 5 = exit
    #

    #  Add password
    if mode == '1':
        print('Add Password')
        pass
    
    #  View password
    elif mode == '2':
        print('View Password')
        pass
    
    #  Modify password
    elif mode == '3':
        print('Modify Password')
        pass
    
    #  Delete password
    elif mode == '4':
        print('Delete Password')
        pass
    
    #  Exit program
    elif mode == '5':
        print('Thank you for using Password Manager!')
        break
    else:
        print("Invalid mode.")
        continue

