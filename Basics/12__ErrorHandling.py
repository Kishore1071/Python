# No error

x = 1

try:

    print(x)

except:

    print("Something went wrong")

else:

    print(f"Value of x is {x}")

finally:

    print("code block executed")



# With error

try:

    print(y)

except:

    print("Something went wrong")

else:

    print(f"Value of x is {y}")

finally:

    print("code block executed")