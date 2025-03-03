class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance of Restaurant
restaurant = Restaurant("Pasta Palace", "Italian")

# Printing the attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creating three different instances of Restaurant
restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, location, favorite_language):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.favorite_language = favorite_language

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Favorite Programming Language: {self.favorite_language}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Creating several instances representing different users
user1 = User("John", "Doe", 30, "New York", "jd@gmail.com")
user2 = User("Jane", "Smith", 25, "London", "janedoe@gmail.com")
user3 = User("Alice", "Johnson", 28, "San Francisco", "alicej@gmail.com")

# Calling both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# 9.13
import random

class Die:
    def __init__(self, sides=6):
        # The number of sides of the die (default is 6)
        self.sides = sides  

    def roll_die(self):
        # Generate a random number between 1 and the number of sides on the die
        roll = random.randint(1, self.sides)
        print(roll)

# Create a 6-sided die
die = Die()

# Roll the die 10 times
for _ in range(10):
    die.roll_die()
