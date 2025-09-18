# names = []

# for i in range(3):                                                          #we use range to make a list
#     names.append(input("Whats your name?"))
    
# for name in sorted(names):
#     print(f"Hello, {name}")
    
name = input("Whats your name? ")
file = open("names.txt", "a")                                                   #open this file beacuse im going to write in it
file.write(f"{name}\n")
file.close()