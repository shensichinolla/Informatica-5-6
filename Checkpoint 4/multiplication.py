def main():
    integer = int(input("Enter a positive integer:"))
    multiplication_table(integer)
    
def multiplication_table(integer):
    i = 1
    while i <= 10:
        result = integer * i
        print(f"{integer} x {i} = {result}")
        i += 1
        

main()      
        
    
    
    
    
