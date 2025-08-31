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
        
try:
    print(calculate("add", 20))
except Exception as e:
    print("Some error occured:",e)
    print(type(e))

