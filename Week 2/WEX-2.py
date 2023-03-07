#
# Weekly Exercise #2: Decisions
# Author: Aditya Dube (G02500368)

pizzas = []

name = input("Enter your name: ")

print("Pizza Size and Cost: Small (10 in, $7.95), Medium (12 in, $9.95), and Large (14 in, $11.95)")
num_pizzas = int(input("Enter the number of pizzas you want to order: "))
size = input("Enter the size of your pizzas (S/M/L): ")

print("Available Topping and Cost Per Topping: Pepperoni, Chicken, Ham, Mushrooms, Onions, Green Peppers, Black Olives, Tomatoes")
toppings = []
if size == "S":
    topping_cost = 0.75
elif size == "M":
    topping_cost = 0.95
else:
    topping_cost = 1.15

num_toppings = int(input("Enter the number of toppings on your pizzas: "))
for i in range(num_toppings):
    topping = input("Enter your choice of topping: ")
    toppings.append(topping)

pizza_cost = 0
if size == "S":
    pizza_cost = 7.95
elif size == "M":
    pizza_cost = 9.95
else:
    pizza_cost = 11.95

subtotal = num_pizzas * pizza_cost + num_toppings * topping_cost
tax = subtotal * 0.06
total = subtotal + tax

if size == 'S':
    size = "Small"
elif size == 'M':
    size = "Medium"
else:
    size = "Large"

print("Order Summary:")
print("Customer name:", name)
print(str(num_pizzas) + " " + size + " pizzas with toppings " + " ".join(toppings))
print("Subtotal: $" + str(subtotal))
print("Sales Tax (6.0%): $" + str(tax))
print("Total Cost: $" + str(total))

