#SyntaxError Example
# print("Hello, world)



#ValueError Example
# try:
#     x = int(input("What´s x? "))
#     print(f"x is equal to {x}")
# except ValueError:
#     print("x is not a number")


#ZeroDivisionError Example
# def spam(divide_by):
#     try:
#         return 42 /divide_by
#     except ZeroDivisionError:
#         print("Error: Invalid Argument")
 


# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


while True:
    try:
        x = int(input("What´s x? "))
    except ValueError:
        print("x is not a number")
    else:
        break
print(f"x is equal to {x}")