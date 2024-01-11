def Addition(*args):

    number_list = []

    string_list = []

    string_data = False

    for x in args:

        if type(x) == str:

            string_data = True
        
            string_list.append(x)

        else:

            number_list.append(x)

    if string_data == False:

        if sum(number_list) == 0:

            return "This function requires minimum one number or character as parameter"

        else:
            
            return sum(number_list)
    
    elif string_data == True:

        sentance = ""

        for y in string_list:

            sentance = sentance + y + " "

        if sum(number_list) == 0:

            return sentance.strip()
        
        else:

            return f"{sum(number_list)}, {sentance.strip()}"

result = Addition("uiyyu", "nbhb ")

print(result)
