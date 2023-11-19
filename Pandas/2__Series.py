import pandas
import string

# Series are like single column


numbers = [1, 2, 3, 4, 5]

number_series = pandas.Series(numbers)

# print(number_series)
# print(number_series[0])  # Index accessing

def DynamicList():

    alphabet = string.ascii_uppercase

    combinations = []

    for char1 in alphabet:
        for char2 in alphabet:
            for char3 in alphabet:
                for char4 in alphabet:
                    combination = char1 + char2 + char3 + char4
                    if len(combinations) < len(numbers):
                        combinations.append(combination)

    return combinations

dynamic_indexing = pandas.Series(numbers, DynamicList())

print(dynamic_indexing)


# # Dictionaries

calories = {"day1": 420, "day2": 380, "day3": 390}

# print(pandas.Series(calories))
# print(pandas.Series(calories, index = ["day1", "day2"]))  # To get only selected index

