"""Lambda is a small anonymous function which is used as a shorthand. Lambda can take many parameter but can handle only one expression"""

# Basic

Double = lambda a, b: (a + b) * 2

print(Double(10, 20))

# def Double(a):

#     return a * 2

# print(Double(10))

# Add = lambda a, b, c : (a + b) * c

# print(Add(5, 6, 3))


# List Comprehension

number_list = [23,54,23,659,32,67,231,45,3,1,43,5,2,23,5,2,4,56,4,2,34]

new_list = [x for x in number_list if x > 10]

print(new_list)
