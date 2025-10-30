def main():
    fuel()
    

def fuel():
    condition = True
    while condition:
        try:
            fraction = input("Fuel fraction: ").split("/")
            num = int(fraction[0])
            den = int(fraction[1])
            percentage = round((num/den)*100)
            if percentage > 100:
                print("Invalid input, percentage for fuel capacity cannot be larger than 100%")
            elif percentage >= 99:
                print("F")
                condition = False
            else:
                print(f"The percentage is: {percentage}%")
                condition = False
        except (ZeroDivisionError,IndexError):
            print("Invalid fraction")
        except ValueError:
            print("Please type numbers, not words")
                     
            print(f"The percentage is:", {percentage})
            condition = False
        except ZeroDivisionError:
            print("Invalid fraction")
        
            
    
main()