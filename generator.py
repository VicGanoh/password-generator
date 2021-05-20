import random 

# create a variable for characters, special characters, upper and lowercase letters
char_ = "qwertyuioplkjhgfdsazxcvbnmPOIUYTREWQASDFGHJKLZXCVMNB0123456789!@#$%^&*()_+-~,./';|\][}{:?><"
# Set minimum_password_length
minimum_password_length = 10

def create_password(password, password_length):
    
    for x in range(0,password_length):     
        password_char = random.choice(char_)
        # Add character to our password variable
        password = password + password_char
    print('Here is your password: ' + password)   

print('Welcome to password generator.\nGenerate your password.')  

try:    
    password_len = int(input("Enter the length of the password you want (minimum length(10)): "))
    password = ""
    if password_len >= minimum_password_length:
        # function call
        create_password(password, password_len)
    else: 
        while password_len < minimum_password_length: 
            try:    
                print("Try Again.")
                password_len = int(input("Enter the length of the password you want (minimum length(10)): "))
                password = ""
                if password_len >= minimum_password_length:
                    # function call
                    create_password(password, password_len)
            except ValueError as e:
                print("Invalid Entry!")
            break
except:
     print("Invalid Entry!")           
    



