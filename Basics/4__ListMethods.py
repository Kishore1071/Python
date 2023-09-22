animals = ['Lion', 'Tiger', 'Leopard', "Jaguar", "Dear", "Wolf", "Fox"]
number_list = [43,12,67,9,34,75,34,5]

data_set1 = [1, 2, 3]
data_set2 = [4, 5, 6]


# Accessing  [This is the only method available for tuple datatype]

animals[3]


# Updating

animals[1] = "Wild Dog"


# Add as last element

animals.append("Elephant")


# Remove last element

animals.pop()


# Add at selected index

animals.insert(1, "Polar Bear")


# Remove selected index

animals.pop(4)


# Asending order

number_list.sort()


# Desending order

number_list.sort(reverse=True)


# Empty a list

number_list.clear()


# Adding list

new_dataset = data_set1 + data_set2


# Find the index of a value

animals.index("Dear")


# Length

len(animals)