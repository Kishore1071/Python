number = int(input("Enter any number: "))

number = str(number)

number_length = len(number)

new_list = []

total = 0

for n in number:

    value = int(n) ** number_length

    total = total + value

    new_list.append(value)

print(new_list)

if int(number) == sum(new_list):

    print("Armstrong number")

else:

    print("Not an armstrong number")
