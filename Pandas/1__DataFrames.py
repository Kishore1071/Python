import pandas

# print(pandas.__version__)

# DataFrames is used to create a table of rows and columns


student_details = {
  'name': ["Rohit", "Virat", "Dhoni"],
  'Maths': [70, 75, 80]
}

table = pandas.DataFrame(student_details)

# print(table)

# print(table.loc[2])  #  accessing row index

# print()

print(table.loc[[0, 2]])  # accessing multiple row index






