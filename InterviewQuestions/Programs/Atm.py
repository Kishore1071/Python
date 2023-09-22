user_data = {
    "username": "Kishore",
    "pin": 1234,
    "balance": 50000,
    "phone_number": 9874561230,
    "otp": 5678
}

while True:

    user_name = str(input("Enter your user name : "))

    if user_name == user_data['username']:

        menu_option = int(input("[1] Widthdraw [2] Balance Enquiry [3] Change Pin [4] Cancel : "))

        if menu_option == 1:

            request_amount = int(input("Enter amount : "))

            if request_amount <= user_data['balance']:

                user_pin = int(input("Enter your pin : "))

                if user_pin == user_data['pin']:

                    new_balance = user_data['balance'] - request_amount

                    user_data['balance'] = new_balance

                    print(f"Transcation Completed, collect your cash. Your available balance is {user_data['balance']}. Thank You!")

                else:

                    print("Invalid pin, try again!")

            else:

                print("Requested amount is higher than your account balance, try again!")

        elif menu_option == 2:

            user_pin = int(input("Enter your pin : "))

            if user_pin == user_data['pin']:

                print(f"Your available balance is {user_data['balance']}.")

            else:

                print("Invalid pin, try again!")

        elif menu_option == 3:

            user_phone_number = int(input("Enter your registered mobile number : "))

            if user_phone_number == user_data["phone_number"]:

                user_otp = int(input("Enter the otp sent to your registered mobile number : "))

                if user_otp == user_data["otp"]:

                    new_pin = int(input("Enter new pin number : "))

                    user_data['pin'] = new_pin

                    print(f"Your pin number updated to {user_data['pin']}")

                else:

                    print("Invalid otp, try again!")

            else:

                print("Invalid phone number, try again!")

        elif menu_option == 4:

            print("Thank you!")

        else:

            print("Invalid option, try again!")

    else:

        print("Invalid username!")

