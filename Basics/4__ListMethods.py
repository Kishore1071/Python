animals = ['Lion', 'Tiger', 'Leopard', "Jaguar", "Dear", "Wolf", "Fox"]
number_list = [43,12,67,9,34,75,34,5]


# Accessing  [This is the only method available for tuple datatype]

print(animals[3])


# Updating

animals[1] = "Wild Dog"

print(animals)


# Add as last element

animals.append("Elephant")

print(animals)



# Remove last element

animals.pop()

print(animals)

animals.pop(2)

print(animals)


# Add at selected index

animals.insert(1, "Polar Bear")

print(animals)


# # Remove selected index

# animals.pop(4)


# Asending order

number_list.sort()

print(number_list)


# Desending order

number_list.sort(reverse=True)

print(number_list)


# Empty a list

number_list.clear()

print(number_list)


# Adding list

data_set1 = [1,2,3]
data_set2 = [1,2,3]

new_dataset = data_set1 + data_set2

print(new_dataset)


# Find the index of a value

print(animals.index("Dear"))


# Length

print(len(animals))