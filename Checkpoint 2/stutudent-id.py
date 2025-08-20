def main():
    print('')
    print('Please enter the following information to create your ID Card.')
    input('Press enter to continue.')
    
    firstname = input("What is your first name? ")
    lastname = input("What is your last name? ").capitalize()
    emailadress = input("What is your email adress? ")
    phonenumber = input("What is your phone number? ")
    idnumber = input("What is your student id number? ")
    fptclass = input("What is your FPT class? ")
    graduationyear = input("What is your expected graduation year? ")
    favsubject = input("What is your favorite subject? ")
    extracurricularac = input("Do you have any extracurricular activities? ")
    
	

    print(f"Your ID Card is")
    line = "-" * 50
    print(line)
    print(lastname), (firstname)
    print(f"Student")
    print(idnumber)
    print(emailadress)
    print(phonenumber)
    print(f"FPT Class: ")
    print(fptclass)
    print(graduationyear)
    print(favsubject)
    
    
    
    
	


    
main()