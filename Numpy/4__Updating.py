import array, numpy

list_items = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list_items)

new_array = array.array('i', list_items)

new_array.append(10)

converted = numpy.array(new_array)

print(new_array)
print(converted)