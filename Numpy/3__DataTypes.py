"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""

import numpy

first_array = numpy.array([{'name': "Kishore"}, 1])

second_array = first_array.copy()

print(second_array)