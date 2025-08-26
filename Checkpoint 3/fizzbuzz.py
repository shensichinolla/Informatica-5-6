def main():
    number = input("Please write a number ")
    if int(number) % 3 == 0 and int(number) % 5 == 0:
        print("FizzBuzz!")
    elif int(number) %3 == 0:
        print("Fizz!")
    elif int(number) %5 == 0:
        print("Buzz!")
    
 
main()