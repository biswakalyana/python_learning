#x = "hello"
#print(x)


try:
    print(x)
except NameError:
    print("Please check if variable X has been defined")
except:
    print("some other exception has happened")