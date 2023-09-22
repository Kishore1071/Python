while True:

    number =  int(input("Enter a number : "))

    result = True

    if number <= 1:

        result = False

    else:

        for a in range(2, number):

            value = number % a

            if value == 0:

                result = False

                break

    if result == True:

        print("Prime Number")

    else:

        print("Not a prime number")










