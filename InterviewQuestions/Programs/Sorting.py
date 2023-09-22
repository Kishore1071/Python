main_list = [242,5,77,43,87,23,6,342,7,1,3,5,6,0,9]

new_list = []

while len(main_list) > 0:

    min_number = min(main_list)

    # index = main_list.index(min_number)

    index = 0

    for a in main_list:

        if a == min_number:

            break

        else:

            index = index + 1

    new_list.append(min_number)

    main_list.pop(index)

print(new_list)
