def main():                                                     # Run the program
    message = input("Enter a message: ").lower()                # Ask user input and then  convert to lowercase                               
    encode_message(message)                                     # Call the function to encode the message   

def encode_message(text):                                       # Function to encode the message
   alphabet = "abcdefghijklmnopqrstuvwxyz"                      # Define the alphabet
   cipher = "zyxwvutsrqponmlkjihgfedcba"                        # Define the reversed alphabet
   new_message = ""                                             # Store the nre message
   i = 0                                                        #So the counter starts with 0 and not 1
   
   while i < len(text):                                         # Do this with every character in the text 
       char = text[i]                                           #Put the first characater in position 0
       
       if char in alphabet:                                      #To see if the character is in the alphabet
           cipher_index = alphabet.find(char)                    #Find the posotion of each character in the alphabet
           new_message += cipher[cipher_index]                   #Replace the character with one of the reversed alphabet
       else:                                                     #If the character is not in the alphabet
           new_message += char                                  #Keep the character the same   
       i += 1                                                   #Go to the next character, add 1
   print("Encoded message:" + new_message)                      #Print the new message
main()                                                          #go to the main function to run the program