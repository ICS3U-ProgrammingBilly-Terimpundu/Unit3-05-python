# Created by Billy Terimpundu
# Created on December 2021
# This program gets the user to enter an number
# between 1 and 12 and tells them the corresponding month.

def main():
    user_number = int(input("Enter your number: "))

    if user_number > 12:
        print("Number must be between 1 and 12!")

    elif user_number < 1:
        print("Number must be between 1 and 12!")

    elif user_number == 1:
        print("January")

    elif user_number == 2:
        print("Febuary")

    elif user_number == 3:
        print("March")

    elif user_number == 4:
        print("April")

    elif user_number == 5:
        print("May")

    elif user_number == 6:
        print("June")

    elif user_number == 7:
        print("July")

    elif user_number == 8:
        print("August")

    elif user_number == 9:
        print("September")

    elif user_number == 10:
        print("October")

    elif user_number == 11:
        print("November")

    elif user_number == 12:
        print("December")

    else:
        print("Invalid entry")


if __name__ == "__main__":
    main()