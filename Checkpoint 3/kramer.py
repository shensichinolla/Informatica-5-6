while True:
    greeting = input("Type a greeting: ")

    if greeting.startswith("hello"):
        print("You won $0.00 dollars")
    elif greeting.startswith("h"):
        print("You won $20.00 dollars")
    else:
        print("You won $100.00 dollars")
        break

