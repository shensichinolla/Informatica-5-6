# names = []

# for i in range(3):                                                          #we use range to make a list
#     names.append(input("Whats your name?"))
    
# for name in sorted(names):
#     print(f"Hello, {name}")
    
# name = input("Whats your name? ")
# file = open("names.txt", "a")                                                   #open this file beacuse im going to write in it
# file.write(f"{name}\n")
# file.close()

with open("names.txt", "a") as file:
    file.write(f"{input("What´s your name?")}")
    
with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines: 
    print(f"Hello {line.rstrip()}")                                             #rstrip removes spaces at the end of the line