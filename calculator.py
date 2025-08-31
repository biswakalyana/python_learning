def calculate(operation , num1, num2):
    if operation == "add":
        return(num1 + num2)
    elif operation == "substract":
        return(num1 - num2)
    elif operation == "multiply":
        return(num1 * num2)
    else:
        print("invalid operaton")
        return
    print("Calcutaor exit")
        
print(calculate("add", 20, 5))
print(calculate("substract", num2=20,num1=5))
print(calculate("multiply",20,5))

