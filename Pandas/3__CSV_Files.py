import pandas

csv = pandas.read_csv('data.csv')

# print(csv)
print(csv.to_string()) # to print all rows without hiding

# print()

# print(csv.head(10))  # To set the row limit 
# print(csv.head())  # To get first 5 rows
# print(csv.tail())  # To get last 5 rows

# print(pandas.options.display.max_rows)  # Maximum rows that can be display without hiding

# # To Alter default

# pandas.options.display.max_rows = 10000
# print(pandas.options.display.max_rows)  # Maximum rows that can be display without hiding


# print(csv.info())