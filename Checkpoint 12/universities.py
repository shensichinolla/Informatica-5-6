print("Welcome to University Fair!!")
print("Universities available: EAC, UACJ, Tecnologico de Monterrey, La Salle, UTP")
user = input("Which university do you want to know about?")

universities = {
    "EAC": {"distance": 404.4,"num_majors": 90,"price": 8370},
    "UACJ": {"distance": 11.3, "num_majors": 57, "price": 3800},
    "Tecnologico de Monterrey": {"distance": 274.7,"num_majors":45,"price": 135000},
    "La Salle": {"distance": 299.7, "num_majors": 35,"price":60000},
    "UTP": {"distance":5, "num_majors": 4, "price": 2505}
}

def main():
    if user == "EAC":
        print(universities["EAC"]["distance"],["num_majors"],["price"])
    elif user == "UACJ":
        print(universities["EAC"]["distance"],["num_majors"],["price"])
    elif user == "Tecnologico de Monterrey":
        print(universities["EAC"]["distance"],["num_majors"],["price"])
    elif user == "La Salle":
        print(universities["EAC"]["distance"],["num_majors"],["price"])
    elif user == "UTP":
        print(universities["EAC"]["distance"],["num_majors"],["price"])
    else:
        print("That´s not a valid university, sorry.")

main()
