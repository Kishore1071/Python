# Append Method: adds new data with existing data

# file = open("textfile.txt", "a")

# file.write("\nI'm Kishore")

# file.close()

# file = open("textfile.txt", "r")

# print(file.read())

# file.close()


# Write Method: Clears old content and only keep the new content


file = open("textfile.txt", "w")

file.write("New")

file.close()

file = open("textfile.txt", "r")

print(file.read())

file.close()