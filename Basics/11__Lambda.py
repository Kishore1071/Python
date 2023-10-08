"""Lambda is a small anonymous function which is used as a shorthand. Lambda can take many parameter but can handle only one expression"""

# Basic

GetName = lambda name: name

# print(GetName("John"))

Add = lambda a, b, c : (a + b) * c

# print(Add(5, 6, 3))


# List Comprehension

number_list = [23,54,23,659,32,67,231,45,3,1,43,5,2,23,5,2,4,56,4,2,34]

new_list = []

for a in number_list:

    if a > 10:

        new_list.append(a)

print(new_list)
