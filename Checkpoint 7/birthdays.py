birthdays = {
    "Aileen" : "October 1st",
    "Mellissa" : "March 15th",
    "Renata" : "March 29th"
}
name = input("Whos birthday do you want to know?: ").capitalize()
if name in birthdays:
    print(f"{name}´s birthday is {birthdays[name]}")