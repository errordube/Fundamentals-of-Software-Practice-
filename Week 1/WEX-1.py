#
# Weekly Exercise #1: Variables, Assignments, and Input/Output
# Aditya Dube (G02500368)

import math

#
# Problem 1: Place the code for this problem below
#
print("---Program Number 1---")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
#The Sum
summing = num1 + num2
print("The sum is: ", summing)
#The Difference
diff = num1 - num2
print("The Difference is: ", diff)
#The Product
pro = num1*num2
print("The Product is: ", pro)
#The Average
avg = (num1 + num2)/2
print("The Average is: ", avg)
#The distance (the absolute value of the difference)
distance = abs (diff)
print("The Aboslute Value of the difference is: ", distance)
#The maximum (the larger of the two)
maxi = max(num1, num2)
print("The Maximum of two is: ", maxi)
#The minimum (the smaller of the two)
mini = min(num1, num2)
print("The Minimum of two is: ", mini)





#
# Problem 2: Place the code for this problem below
#
print("---Program Number 2---")
Length = (input("Enter Length: "))
Length=int(Length)
Width = (input("Enter Width: "))
Width = int(Width)
#Rectangle Area
area = Length * Width
print("The Area of rectangle is: ", area)
#Rectangle Perimeter
peri = (2*Length) + (2* Width)
print("The Perimeter of rectangle is: ", peri)
#Length of Diagnol 
D = math.sqrt(Length**2 + Width**2)
print("Length of Diagnol is: ", D)



#
# Problem 3: Place the code for this problem below
#

print("---Program Number 3---")
gallons = float(input("Enter no of gallons of gas in tank: "))
efficiency = float(input("Enter fuel efficiency in miles: "))
price = float(input("Enter price of gas per gallon: "))
cpm = (100/efficiency) * price
distance = gallons * efficiency
print("Cost per 100 miles: ", cpm)
print("The car can travel ", distance , "miles")
