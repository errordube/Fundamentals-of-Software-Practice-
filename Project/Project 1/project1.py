import math

#
# CIS 500, Winter 2023, Project 1
# Author: Aditya Dube (G02500368)

#
# Function that computes and returns monthly car payments given three inputs: the principal,
# annual interest rate (such as 6.0 for 6%), and the total number of payments (such as 324, 6, 48, or 60).
# 
# The formula for calculating the monthly payment is:
#       payment = (i * p) / (1 - (1 + i) ** (-n))
#
#       where p = principal
#             i = monthly interest rate (calculated as annual interest rate / 1200)
#             n = total number of payments
#
def monthly_car_payment(principal, annual_interest_rate, tot_nbr_of_payments):
    #convert annual to monthly interest rate
    monthly_rate = annual_interest_rate/12/100
    monthly_payment = (principal*monthly_rate) / (1-(1+monthly_rate)** (-tot_nbr_of_payments))
    return monthly_payment


#
# Function that takes a nonnegative integer as input, computes n! using Gosper's formula,
# and returns it.
# 
# Gosper's formula to approximate n! is:
#       n! = (n ** n) * (math.e ** -n) * math.sqrt((2*n + 1/3) * math.pi)
#
def n_factorial(n):
    return float((n**n) * (math.e ** -n) * math.sqrt((2*n + 1/3) * math.pi))


#
# Easter Sunday is the first Sunday after the first full moon of spring. To compute
# the date, you can use the following algorithm, invented by the mathematician
# Carl Friedrich Gauss in 1800.
#
#  1. Let y be the year (such as 1800 or 2001). This is the input to the function.
#  2. Divide y by 19 and call the remainder a. Ignore the quotient.
#  3. Divide y by 100 to get a quotient b and a remainder c.
#  4. Divide b by 4 to get a quotient d and remainder e.
#  5. Divide 8 * b + 13 by 25 to get a quotient g. Ignore the remainder.
#  6. Divide 19 * a + b - d - g + 15 by 30 to get a remainder h. Ignore the quotient.
#  7. Divide c by 4 to get a quotient j and a remainder k.
#  8. Divide a + 11 * h by 319 to get a quotient m. Ignore the remainder.
#  9. Divide 2 * e + 2 * j - k - h + m + 32 by 7 to get a remainder r. Ignore the quotient.
# 10. Divide h - m + r + 90 by 25 to get a quotient n. Ignore the remainder.
# 11. Divide h - m + r + n + 19 by 32 to get a remainder p. Ignore the quotient.
#
# Then Easter falls on day p of month n.
#
# The function takes a year as input and returns a string containing the month and day of
# Easter Sunday of that year. For example, if the input to the function is 2001, then
# the function returns the string "April 15".
#
# Complete the "TO DO" section of the function below. Keep the rest of the code as is.
#
def easter_sunday(y):
    months = ['NA', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                'September', 'October', 'November', 'December']
    
    # TO DO: Insert your code here
    
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19*a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    L = (32 + 2*e + 2*i - h - k) % 7
    m = (a + 11*h + 22*L) // 451
    n1 = (h + L - 7*m + 114) // 31
    p1 = ((h + L - 7*m + 114) % 31) + 1
    

    return months[n1] + ' ' + str(p1)


#
# The original U.S. income tax of 1913 was quite simple. The tax was
#       1 percent on the first $50,000
#       2 percent on the amount over $50,000 up to $75,000
#       3 percent on the amount over $75,000 up to $100,000
#       4 percent on the amount over $100,000 up to $250,000
#       5 percent on the amount over $250,000 up to $500,000
#       6 percent on the amount over $500,000
#
# Function takes income of a taxpayer as input, computes, and returns the income tax
# according to the above schedule.
#
def income_tax(income):
    if income <= 50000:
        return income * 0.01
    elif income <= 75000:
        return (income - 50000) * 0.02 + 50000 * 0.01
    elif income <= 100000:
        return (income - 75000) * 0.03 + (75000 - 50000) * 0.02 + 50000 * 0.01
    elif income <= 250000:
        return (income - 100000) * 0.04 + (100000 - 75000) * 0.03 + (75000 - 50000) * 0.02 + 50000 * 0.01
    elif income <= 500000:
        return (income - 250000) * 0.05 + (250000 - 100000) * 0.04 + (100000 - 75000) * 0.03 + (75000 - 50000) * 0.02 + 50000 * 0.01
    else:
        return (income - 500000) * 0.06 + (500000 - 250000) * 0.05 + (250000 - 100000) * 0.04 + (100000 - 75000) * 0.03 + (75000 - 50000) * 0.02 + 50000 * 0.01


#
# Function that takes a person's weight in pounds and height in inches
# and calculates the person's body mass index (BMI). It then uses the BMI
# to categorize the person's weight status as "Underweight", "Normal",
# "Overweight", or "Obese". The function returns the weight status as
# its return value.
#
# The BMI is calculated using the following equation:
#
#   BMI = (703 * weight) / height^2
#
# The weight categorization is done based on the following table from the
# United State's Center for Disease Control:
#
#   BMI                 Weight Status
#   Below 18.5          Underweight
#   Below 25.0          Normal
#   Below 30.0          Overweight
#   >= 30.0             Obese
#
def bmi_category(weight, height):
    BMI = (703*weight) / (height*height)
    if BMI < 18.5:
        return "Underweight"
    elif BMI < 25.0:
        return "Normal"
    elif BMI < 30.0:
        return "Overweight"
    else:
        return "Obese"


#
# Function that takes month, day, and year values for a date in
# Gregorian calendar (calendar used in most of the world) and
# returns the day number (1 to 366) of that date. The code must
# be able to handle dates in a leap year.
# 
# To make it easier for you, is_leap_year() function defined below
# can be used to check if a year is a leap year.
# 
def day_number_of_date(month, day, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_in_month[2] = 29
    day_number = 0
    for i in range(1, month):
        day_number += days_in_month[i]
    day_number += day
    return day_number      

#
# THIS FUNCTION IS DONE FOR YOU - DON'T MAKE ANY CHANGES
#
# Function that determines if a year is a leap year using the
# following logic - a year is a leap year if it is divisible by four,
# except that any year divisible by 100 is a leap year only if it is
# divisible by 400.
#
# The function returns True if the year is a leap year or False otherwise
#
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


#
# Function that takes a nonnegative integer (>= 0), converts that value to its
# binary representation (store it as a string of bits), and returns that string.
#
# Find (or figure out) an algorithm to convert a decimal number to a binary number
# and use it to implement this function.
#
# You are not allowed to use the built-in functions bin() or format() in your implementation.
#
def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    binary = ""
    while decimal >= 1:
        remainder = decimal % 2
        decimal = decimal // 2
        binary = str(remainder) + binary
    return binary


#
# Function that takes a string representing a nonnegative integer
# in binary representation, converts it to its decimal equivalent, and
# return that value.
#
# You can assume that the input string nonempty and contains only 1s and 0s.
#
# Find (or figure out) an algorithm to convert a binary number to a decimal number
# and use it to implement this function.
#
# You are not allowed to use the int(str,2) built-in function in your implementation.
#
def binary_to_decimal(binary_str):
    decimal = 0
    binary_str = str(binary_str)
    for digit in binary_str:
        decimal = decimal*2 + int(digit)
    return decimal


#
# A prime number is a natural number greater than 1 that has only two factors, that are,
# 1 and the number itself. A prime number is not divisible by any other number except
# 1 and itself.
# 
# Function takes a positive integer (>= 1) as input and returns True if the number is prime, False otherwise.
# 
# You are free to find, understand, and code any algorithm for checking if a number is a prime number.
#
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True


#
# Function takes a positive integer and returns a string containing all prime numbers
# up to that integer.
#
# For example, if input is 20, then the function returns the string "2 3 5 7 11 13 17 19"
#
# You must make use of is_prime() function above in your implementation.
#
def prime_numbers(n):
    primes = ""
    for num in range(2, n+1):
        if is_prime(num):
            primes += str(num) + " "
    return primes.strip()
    



#
# Driver function where you can write test calls to functions as you develop each function
#
def main():
    # some example function calls
    print(monthly_car_payment(20000,6,36))
    print(easter_sunday(2001))
    print(prime_numbers(20))
    print(bmi_category(145,65))
    print(income_tax(350000))
    print(n_factorial(4))
    print(day_number_of_date(2,28,2021))
    print(decimal_to_binary(4))
    print(binary_to_decimal('100'))
    print(is_prime(1))

#
# call main() function if this script is run as a main program
#
if __name__ == '__main__':
    main()
