result = 0

def calculate(operation , num1, num2):
    global result
    if operation == "add":
        result = num1 + num2
    elif operation == "substract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    else:
        print("invalid operaton")
        return
    return result
    print("Calcutaor exit")

calculate("add", 20, 5)
print(result)  