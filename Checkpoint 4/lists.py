independence_stages = ["Inicio", "Organizacion", "Resistencia", "Consumacion"]
print(independence_stages[0])                                   #Print the first element
print(len(independence_stages))                                  #Print the length of the list



#List methods
leaders = []
leaders.append("Miguel Hidalgo") 
leaders.append("Vicente Guerrero")
# leaders.extend(independence_stages)           #Mix both lists together
leaders.insert(1, "Jose Maria Morelos y Pavon") #To put it in an specific position
# leaders.remove("Vicente Guerrero")            #To delete an element
leaders.append(input("Type a leader:"))
# leaders.pop(1)                                #To delete an element in a specific position
# leaders.clear()                                 #To delete all the list
leaders.index("Miguel Hidalgo")                #To know the position of an element
leaders.count("Vidente Guerrero")               #To count how many times an element is in the list
print(leaders.index("Miguel Hidalgo"))                      
print(leaders.count("Vicente Guerrero"))
# leaders.sort()                              #To order the list
# leaders.reverse()
new_leaders = leaders.copy()
print(leaders)
print(new_leaders)