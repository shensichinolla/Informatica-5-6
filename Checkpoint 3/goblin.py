import random
print(" Welcome to the goblin game ")
print("THE BEST GAME EVER! ")
player_name = input("What is your name? ")
print(player_name , "can you find the goblin? ")
print("|_||_||_||_||_|")
goblin_position = random.randint(1, 5)
keep_trying = True
while keep_trying:
    guessed_position = int(input("Can you guess where the goblin is? "))

    if guessed_position == goblin_position:
        print("Good job, you found the goblin:)")
        keep_trying = False
    else: print("Your guess is wrong:(")

