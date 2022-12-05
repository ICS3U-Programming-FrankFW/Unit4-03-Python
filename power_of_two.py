#!/usr/bin/env python3
# Created By: Frankie
# Date: Nov. 15, 2022
# This program returns the guess to the user
# The input number and all other numbers preceding it.

import math


def main():

    # Casts the user's number as a string

    num_as_string = input("Enter a number: ")

    # This is casting the user's number to an integer

    try:

        user_int = int(num_as_string)

    # Tells the user to restart if they did not enter a number

    except ValueError:

        input("Please enter a positive integer. Please retry.")

    if user_int < 0:

        input("Please enter a positive integer. Please try again.")

    # Loops through code until counter is equal to user_int

    for counter in range(1, user_int + 1, 1):

        print(f"Looped through {counter} times.")

        squared = math.pow(counter, 2)

        print(f"{counter}^2 = {squared}")


if __name__ == "__main__":
    main()
