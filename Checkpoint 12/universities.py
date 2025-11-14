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
    name = input("Type the name of the university: ")
    if name not in universities:
        print("Sorry, that university is not in our list.")
    else:
        uni = universities[name]
    print(uni)
    api = requests.get("http://universities.hipolabs.com/search?name="+universities[uni]["officiald_name"])
    print(api.json())

main()
