def main():
    len_list = int(input("Enter how many numbers you wanto to put in the list:"))
    number_list = []
    
    for i in range(len_list):
        list_element = int(input("Enter a number:"))
        number_list.append(list_element)
        
    print(number_list)
    with open("numbers.txt", "a") as file:
        for number in number_list:
            file.write(f"{number}\n")
    
    greater = max(number_list)
    print("The greatest number in the list is:", greater)
    
main()