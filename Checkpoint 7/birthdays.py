birthdays = {
    "Aileen" : "October 1st",
    "Mellissa" : "March 15th",
    "Renata" : "March 29th"
}

name = input("Whos birthday do you want to know?: ").capitalize()
if name in birthdays:
    print(f"{name}´s birthday is {birthdays[name]}") 
else:
    print(f"I don´t have that birthday information")
    new_birthday = input(f"When is  {name}´s bithday?: ").capitalize()
    birthdays[name] = new_birthday
    print("Birthday database updated.")
print(birthdays)