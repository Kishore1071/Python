while True:

    number = int(input("Enter a number : "))

    number_string = str(number)

    result = 0

    for a in number_string:

        value = int(a) ** int(len(number_string))

        result =  result + value

    if result == number:

        print("Armstrong Number")

    else:

        print("Not a armstrong number")

        

