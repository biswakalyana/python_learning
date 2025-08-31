try:
    result = exec("10 / 0")
    print(result)
    x,y = "10","5"
    print(int(x) + int(y))
except SyntaxError:
    print("Please check your Syntax")
except ValueError:
    print("value provided to calculation is incorrect")
except ZeroDivisionError:
    print("you are dividing a number with 0, which is not possible")
except Exception as e:
    print("Some unknown exception has happened")
    print(e)
    print(type(e))


