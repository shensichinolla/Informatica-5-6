my_list =[5, 2, 3, 1, 4]                     # . = METODO () = FUNCION
my_list2 = ["a", "b", "c"]
greatest = max(my_list)              #MAX is to find the greate number in the list
print("The greatest number in the list is:", greatest)

smallest = min(my_list)              #MIN is to find the smallest number in the list
print("The smallest number in the list is:", smallest)

list_sum = sum(my_list) 
print("The sum of all numbers in the list is:", list_sum)  #SUM is to find the result when you add all numbers in the list

list_length = len(my_list)          #LEN is to find the length of the list
print("This list has", list_length, "elements")

order = sorted(my_list)             #SORTED is to order the list from smallest to greatest
print("The list in order is :", order)

def filter_price(price): #Define filter_price function
    if (price >= 400):   #Condition to filter prices less than 400
        return True     #if it is true keep it
    else:
        return False    #if it is not delete it
item_price = [230, 400, 450, 350, 370] 
filtered_price = filter(filter_price, item_price)   #FILTER is to filter the list with a condition
print(list(filtered_price))  #Convert the filter object to a list and print it
