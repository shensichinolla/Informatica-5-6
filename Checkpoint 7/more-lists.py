# names = ["Bob", "Alex", "Kevin"]
# names.append("Joseph")

# for name in sorted(names):
#     print(name)


# List with floats
# measurements = [-2.5, 1.1, 7.5, 14.6, 21.0, 19.2]
# mean = sum(measurements) / len(measurements)
# print("The mean is:", mean)

# List within lists
super_list = [[5,2,3],[4,1],[2,2,5,1]]
print(super_list[1][0])

# grades = [["Shakira", 8, "D"], ["Mellisa" , 0, "C"], ["Shensi", 10, "A"]]
# for student in grades:
#     name = student[0]
#     grade = student[1]
#     group = student[2]
#     print(f"{name} has a grade of {grade} from group {group}")

# Matrices
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print rows
for row in matrix:
    print(row)
# print columns
for column in range(3): #repeat for every column, o sea 3 times
    for row in matrix:
        print(row[column])
    
    
    