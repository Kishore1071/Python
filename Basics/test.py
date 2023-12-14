a = "j"

try:

    new = a + "Qwerty"

except:

    print("Datatype error, value of a must be string")

else:

    new = a + "Qwerty"

    print(f"The expected output is {new}")

finally:

    print("Process Completed")