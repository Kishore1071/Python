import numpy
import array

first_array = numpy.array([1, 2, 3, 4, 5])
second_array = numpy.array([[1, 2], [3, 4]])

# Accessing

print(second_array[0, 1])


# Slicing

print(second_array[1, 0:1])


# Arrays datatype

print(first_array.dtype)


# Copy of array [Change in one array never effect the other one]

new_array = first_array.copy()


# View of array [Change in one array effect the other one]

new_array2 = first_array.view()

# Shape of array

two_dimensional_array = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8],])

print(two_dimensional_array.shape)


# Reshape

array0 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(array0.reshape(3,3))


# Looping : As same as normal python for

# Join

array1 = numpy.array([1, 2, 3])
array2 = numpy.array([4, 5, 6])
array3 = numpy.concatenate((array1, array2))

print(array3)


# Split

array4 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

array5 = numpy.array_split(array4, 3)

print(array5)


# Finding the index of value

index_of_array = numpy.where(second_array == 3)

print(index_of_array, "rtyui")


# Sort

print(numpy.sort(array4))









