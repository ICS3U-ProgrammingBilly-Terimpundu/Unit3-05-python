#!/usr/bin/env python3

# Created by Billy Terimpundu
# Created on December 2021
# This program gets the user to enter an number
# between 1 and 12 and tells them the corresponding month.

def main():
    month = int(input("Enter your number: "))

    if month > 12:
        print("Number between 1 and 12!")

    elif month == 1:
        print("January")

    elif month == 2:
        print("Febuary")

    elif month == 3:
        print("March")

    elif month == 4:
        print("April")

    elif month == 5:
        print("May")

    elif month == 6:
        print("June")

    elif month == 7:
        print("July")

    elif month == 8:
        print("August")

    elif month == 9:
        print("September")

    elif month == 10:
        print("October")

    elif month == 11:
        print("November")

    elif month == 12:
        print("December")

    else:
        print("Invalid")


if __name__ == "__main__":
    main()