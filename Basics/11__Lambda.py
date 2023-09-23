"""Lambda is a small anonymous function which is used as a shorthand. Lambda can take many parameter but can handle only one expression"""

# Basic

GetName = lambda name: name

print(GetName("John"))


# List Comprehension

number_list = [23,54,23,659,32,67,231,45,3,1,43,5,2,23,5,2,4,56,4,2,34]

new_list = [number for number in number_list if number > 10]

print(new_list)
