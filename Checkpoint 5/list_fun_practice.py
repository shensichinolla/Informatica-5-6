my_list = [9, 4, 2, 11, 18]

def list_length(my_list): 
    list_length = len(my_list)
    return list_length
print(list_length(my_list))

def mean_list(my_list):
    mean_list = sum(my_list)/list_length(my_list)
    return mean_list
print(mean_list(my_list))

def range_of_list(my_list):
    range_of_list = max(my_list)-min(my_list)
    return range_of_list
print(range_of_list(my_list))

def add_values():
    values = []
