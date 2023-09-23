"""Function is used to reduce repeating code"""

# Basic function

def Check():

    print("Function is  working")

Check()


# Function with parameters and arguments

def Add(number1, number2):

    print(number1 + number2)

Add(10, 15)


# Function with return statement

def Addition(number1, number2):

    return number1 + number2

result = Addition(10, 15)

print(result)


# Accepting unlimited arguments

def AddData(*args, **kwargs):

    print(args)
    print()
    print(kwargs)

AddData()


