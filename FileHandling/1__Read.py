file = open("textfile.txt", "r")

print(file.read())

# To read only limited characters from the file

print(file.read(5))

# To read line by line use the following command for each line , We also can for loop to get line by line

print(file.readline())

# To close file

file.close()