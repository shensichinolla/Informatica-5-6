# key : value                            #a dictionary in python works like:
# capitals = {                             # curly brackets{}
#     "Mexico": "Mexico City",
#     "Canada": "Ottawa",
#     "Brazil" : "Brasília",
#     #"Canada" : "Montreal"                #UNIQUE KEYS
# }

# capitals["Italy"] = "Rome"            #Tadd a new elemet to the dictionary
# del capitals["Brazil"]                #del: delete an elemen
# capitals.pop("Canada")                #.pop is also to delete
# capitals.clear()                      #clear is also to delete all the elements

# print(capitals)

# Excerse 1
# houses = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }
# for students in houses:                           #it will go through each key
#     print(f"{students}: {houses[students]}")      #acessing the value using the key
    
# Complex dictonary
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for student in students:
    print(f"{student["name"]}, {student["house"]}, {student["patronus"]}")
