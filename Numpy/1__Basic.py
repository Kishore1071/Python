import numpy

new_array = numpy.array([1, 2, 3, 4, 5])


print(new_array)
print(type(new_array))
print(numpy.__version__)


# Zero dimensional array

zero = numpy.array(25)
print(zero.ndim, "Zero")


# One dimensional array

one = numpy.array([1, 2, 3])
print(one.ndim, "One")


# Two dimensional array

two = numpy.array([[1, 2], [3, 4]])
print(two.ndim, "Two")