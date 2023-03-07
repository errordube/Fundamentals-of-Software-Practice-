#
# CIS 500, Winter 2023, Project 2
# Author: Aditya Dube (G02500368)

import sys

#
# Function digit_to_code() takes a single-digit integer in the range 0 - 9 (both inclusive)
# as input and returns the bar code (see project specs) of that digit as a string value.
#
# If the input is not in the range 0 - 9, the function raises ValeuError exception with
# "Argument not in range 0 - 9" as the message of exception raised. Validate input(s) first
# before coding normal logic.
#   
def digit_to_code(digit):
    if digit == 0:
        return "||:::"
    elif digit == 1:
        return ":::||"
    elif digit == 2:
        return "::|:|"
    elif digit == 3:
        return "::||:"
    elif digit == 4:
        return ":|::|"
    elif digit == 5:
        return ":|:|:"
    elif digit == 6:
        return ":||::"
    elif digit == 7:
        return "|:::|"
    elif digit == 8:
        return "|::|:"
    elif digit == 9:
        return "|:|::"
    else:
        raise ValueError("Argument not in range 0 - 9")


#
# Function code_to_digit() takes the code of a digit as a string value and returns the
# corresponding digit.
#
# If the input is not a valid digit code, the function raises ValueError exception with
# "Argument not a valid digit code" as the message of exception raised.
#
def code_to_digit(code):
    if code == "||:::":
        return 0
    elif code == ":::||":
        return 1
    elif code == "::|:|":
        return 2
    elif code == "::||:":
        return 3
    elif code == ":|::|":
        return 4
    elif code == ":|:|:":
        return 5
    elif code == ":||::":
        return 6
    elif code == "|:::|":
        return 7
    elif code == "|::|:":
        return 8
    elif code == "|:|::":
        return 9
    else:
        raise ValueError("Argument not a valid digit code")


# 
# Function zipcode_to_barcode() takes a zip code as a string input and returns the
# corresponding bar code as a string value.
#
# The function raises ValueError exception with "Invalid value for zip code" as the
# message of exception if input meets any of these conditions:
#       - input is not a string (use type() function)
#       - input string length is not 5
#       - input string is not numeric
#
def zipcode_to_barcode(zipcode):
    if type(zipcode) != str:
        raise ValueError("Invalid value for zip code")
    if len(zipcode) != 5:
        raise ValueError("Invalid value for zip code")
    if not zipcode.isnumeric():
        raise ValueError("Invalid value for zip code")

    # Convert each digit to a code
    codes = [digit_to_code(int(x)) for x in zipcode]

    # Add check digit
    check_digit = (10 - sum(int(x) for x in zipcode) % 10) % 10
    codes.append(digit_to_code(check_digit))
   # zipcode = zipcode + str(check_digit)


    # Concatenate all codes into a single string
    barcode = "|" + "".join(codes) + "|"

    return barcode


# 
# Function barcode_to_zipcode() takes a bar code as a string input and returns the
# corresponding zip code as a string value.
#
# The function raises ValueError exception with "Invalid value for bar code" as the
# message of exception if input meets any of these conditions:
#       - input is not a string (use type() function)
#       - input string length is not 32
#       - input string is not a valid bar code
#
def barcode_to_zipcode(barcode):
    if type(barcode) != str:
        raise ValueError("Invalid value for bar code")
    if len(barcode) != 32:
        raise ValueError("Invalid value for bar code")
    if barcode[0] != '|' or barcode[31] != '|':
        raise ValueError("Invalid value for bar code")

    barcode = barcode[1:-1]  # remove the frame bars
    codes = [barcode[i:i+5] for i in range(0, len(barcode), 5)]  # split into codes
    zipcode = ''.join([str(code_to_digit(code)) for code in codes])  # convert codes to digits
    check_digit = code_to_digit(barcode[-5:])  # extract the check digit
    if int(zipcode[-1]) != check_digit:
        raise ValueError("Invalid value for bar code")
    return zipcode[:-1]


    
    


#
# Function display_menu() prints the command menu for the program
#
def display_menu():
    print("\n1. Zip Code to Bar Code Conversion")
    print("2. Bar Code to Zip Code Conversion")
    print("3. Quit Program")


#
# Function get_menu_selection() prompts the user for menu item selection and returns
# the user selection.
#
def get_menu_selection():
    while True:
        selection = int(input("\nEnter your selection (1, 2, or 3): "))
        if selection in [1, 2, 3]:
            break
        else:
            print("Invalid input. Try again.")
    return selection
        

#
# Function main() implements command-line interface to zipcode <--> barcdde converter.
#
def main():
    print("Postal Zip Code <--> Postal Bar Code Converter Program")
    while True:
        display_menu()
        selection = get_menu_selection()

        if selection == 1:
            try:
                zipcode = input("Enter a zip code: ")
                barcode = zipcode_to_barcode(zipcode)
                print("The bar code is: " + barcode)
            except ValueError as ve:
                print(ve)

        elif selection == 2:
            try:
                barcode = input("Enter a bar code: ")
                zipcode = barcode_to_zipcode(barcode)
                print("The zip code is: " + zipcode)
            except ValueError as ve:
                print(ve)

        else:
            print("Good Bye")
            break


# run the main() if this module is executed as a top-level script/program
if __name__ == '__main__':
    main()

