import getpass

def main():
    password = getpass.getpass("Please set a password ")
    input('Press enter to continue.')
    check_password(password)
    
def check_password(p):
    guess = input("Enter password ")
    if p == guess:
        print("You know the password! ")
    
    if p != guess:
        print("The password is not correct, the program will close soon ")
    print("The program has ended ")
    
main()

   