# String Formatting

movie = "Avenger Infinity War"

my_favourite_movie = f"My favourite movie is {movie}"

print(my_favourite_movie)


# Multi line string

content1 = """This is 
a 
paragraph
# """

content2 = '''This is 
a 
paragraph
'''


# Slicing

name = "Antony Stark"

print(name[2:6])

print(name[::-1])  # Reverse the string


#  Length

print(len(name))


# Concatination

first_name = "Captain"
last_name = "America"

full_name = first_name + ' ' + last_name

print(full_name)


# Escape Characters

description = "Dark Knight movie was directed by  \"Christopher\" Nolan"

print(description)


# Index accessing of string

car = "Rolls Royce"

print(car[4])


# Coverting string to list

planets = "Mercury Venus Earth Mars Jupiter"

print(planets.split(" "))