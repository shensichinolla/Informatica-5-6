dictionary = {
    "color": "pink",
    "age": 17
}

#Values Method
print(dictionary.values())
for v in dictionary.values():                     #for each value in dictionary.values
    print(v)
    

#Keys Method
print(dictionary.keys())
for k in dictionary.keys():                      #for each key in dictionary.keys
    print(k)
    
#Items Method
print(dictionary.items())
for i in dictionary.items():
    print(i)                                         #for each item in dictionary.items
    
#Prink key and value using methods
#to do

#Get Method
picnic_items = { "apples":5, "cups":2}
print(f"I am bringing {picnic_items.get("cups")} cups.")

print(f"I am bringing {picnic_items.get("cups")} cups.")

#Setting a default value
pet_info = {
    "name": "Cookie",
    "age": 4
}

pet_info.setdefault("color", "white")  #if color is not in the dictionary, set it to white
pet_info["color"] = "black" 
pet_info.setdefault("color", "black")
print(pet_info)