file = open("textfile.txt", "rt")

print(file.read())

# To read only limited characters from the file

print(file.read(1))

# To read line by line use the following command for each line , We also can for loop to get line by line

print(file.readline())

# To close file

print(file.close())