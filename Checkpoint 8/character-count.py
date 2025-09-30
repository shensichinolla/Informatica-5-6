
def character_counter(message,dictionary):
    for character in message:                           #for each character in message
        dictionary.setdefault(character, 0)             #if character is not in the dictionary, set it to 0
        dictionary[character] += 1                      #add 1 
    
    print(dictionary)


message = input("Enter a message: ")
dictionary = {}
character_counter(message,dictionary)                   #call the function
