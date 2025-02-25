favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)

print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print(f"I really love {pizza} pizza!")

print("\nI really love pizza!")

for number in range(1, 21):
    print(number)

# Creating a list of numbers from 1 to 1 million
numbers = range(1, 1000001)

# Using a for loop to print each number (optional: comment out to avoid printing so many numbers)
for number in numbers:
    print(number)

# List of numbers from 1 to 1 million
numbers = range(1, 1000001)

# Use min(), max(), and sum() to check and sum the numbers
print("Min:", min(numbers))  # Should print 1
print("Max:", max(numbers))  # Should print 1000000
print("Sum:", sum(numbers))  # Should print the sum of all numbers from 1 to 1 million

# Using range() to get odd numbers from 1 to 20
for number in range(1, 21, 2):  # Step of 2 for odd numbers
    print(number)

# Using range() to get multiples of 3 from 3 to 30
for number in range(3, 31, 3):  # Step of 3 for multiples of 3
    print(number)

# List of the first 10 cubes
cubes = [value ** 3 for value in range(1, 11)]  # List comprehension to generate cubes

# Print each cube
for cube in cubes:
    print(cube)

# List comprehension to generate the first 10 cubes
cubes = [value ** 3 for value in range(1, 11)]

# Print the list of cubes
print(cubes)

# A list of some numbers (or pizzas, or other items)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# The first three items in the list
print("The first three items in the list are:", numbers[:3])

# Three items from the middle of the list
middle_index = len(numbers) // 2
print("Three items from the middle of the list are:", numbers[middle_index-1:middle_index+2])

# The last three items in the list
print("The last three items in the list are:", numbers[-3:])

# Original list of pizzas
my_pizzas = ["Margherita", "Pepperoni", "Veggie", "Hawaiian"]

# Make a copy of the list
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list
my_pizzas.append("BBQ Chicken")

# Add a different pizza to the friend's list
friend_pizzas.append("Seafood")

# Print both lists to show they are separate
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

# List of food items
foods = ["Pizza", "Burger", "Pasta", "Sushi", "Tacos"]

# First loop to print the list
print("First loop to print the list of foods:")
for food in foods:
    print(food)

# Second loop to print the list again
print("\nSecond loop to print the list of foods:")
for food in foods:
    print(food)

# 1. Define a tuple with five basic foods
menu = ("Pizza", "Burger", "Pasta", "Salad", "Soup")

# 2. Use a for loop to print each food the restaurant offers
print("Original menu:")
for food in menu:
    print(food)

# 3. Try to modify an item in the tuple (This will raise an error)
# menu[0] = "Sushi"  # Uncommenting this line will result in a TypeError because tuples are immutable.

# 4. The restaurant changes its menu, replacing two items with new foods
menu = ("Sushi", "Steak", "Pasta", "Salad", "Tacos")  # Rewriting the tuple

# 5. Print the revised menu
print("\nRevised menu:")
for food in menu:
    print(food)

# Modified Program for Exercise PEP 8

# Define the list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the first three items in the list
print("The first three items in the list are:", numbers[:3])

# Find the middle index and print three items from the middle
middle_index = len(numbers) // 2
print("Three items from the middle of the list are:", 
      numbers[middle_index-1:middle_index+2])

# Print the last three items in the list
print("The last three items in the list are:", numbers[-3:])

# Define the list of favorite pizzas
my_pizzas = ["Margherita", "Pepperoni", "Veggie", "Hawaiian"]

# Make a copy of the list for the friend's pizzas
friend_pizzas = my_pizzas[:]

# Add new pizzas to each list
my_pizzas.append("BBQ Chicken")
friend_pizzas.append("Seafood")

# Print each list of pizzas
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

# List of food items
foods = ["Pizza", "Burger", "Pasta", "Sushi", "Tacos"]

# First loop to print the list of foods
print("First loop to print the list of foods:")
for food in foods:
    print(food)

# Second loop to print the list of foods
print("\nSecond loop to print the list of foods:")
for food in foods:
    print(food)

