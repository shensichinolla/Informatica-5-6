#include <stdio.h>
def hello():
    print("hello")

name = input("What is your name?").title().strip()
hello()
print(f"hello,{name}")

