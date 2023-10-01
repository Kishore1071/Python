import pandas

# Series are like single column


numbers = [1, 2, 3, 4, 5]

number_series = pandas.Series(numbers)

print(number_series)
print(number_series[0])  # Index accessing

dynamic_indexing = pandas.Series(numbers, ['a', 'b', 'c', 'd', 'e'])

print(dynamic_indexing)


# Dictionaries

calories = {"day1": 420, "day2": 380, "day3": 390}

print(pandas.Series(calories))
print(pandas.Series(calories, index = ["day1", "day2"]))  # To get only selected index

