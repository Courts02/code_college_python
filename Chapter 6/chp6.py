#  A simple Dictionary

alien_0 = {'color': 'green', 'points': 5}
# The dictionary alien_0 stores the aliens color and point value
print(alien_0['color'])
print(alien_0['points'])
# these line access and disaply that information in the terminal

# Adding new key value pairs:
# You can add new key-value pairs to a dictionary in 
# Python by using the dictionary name followed by the new key in square brackets, and assigning it a value.

# Define a dictionary
my_dict = {'name': 'Alice', 'age': 25}

# Add a new key-value pair
my_dict['location'] = 'New York'

# Print the updated dictionary
print(my_dict)

# To modify a value in a dictionary, use the dictionary name with the key in square brackets, followed by the new value you want to assign.
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# To remove a key-value pair from a dictionary, use the del statement with the dictionary name and the key to be removed.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# A List of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

#  A List in a Dictionary

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
 # Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

# You can nest dictionaries by using a key (e.g., username) and storing related information
#  (like name and location) in a nested dictionary. Access the data by looping through the outer dictionary.

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():

    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")