# 8.1
def display_message():
    print("I am learning about functions in Python.")

# Call the function to display the message
display_message()

# 8.2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Call the function with a book title
favorite_book("Alice in Wonderland")

# 8.3
# Function definition
# def make_shirt(size, message):
# message}'.")

# # Calling the function using positional arguments
# make_shirt("L", "Python is awesome!")

# # Calling the function using keyword arguments
# make_shirt(size="M", message="Coding is fun!")

# # 8.4
# # Function definition with default values for size and message
# def make_shirt(size="L", message="I love Python"):
#     print(f"The shirt is size {size} and it has the message: '{message}'.")

# # Creating a large shirt with the default message
# make_shirt()

# # Creating a medium shirt with the default message
# make_shirt("M")

# # Creating a shirt of any size with a custom message
# make_shirt("S", "Coding is life!")

# 8.5
# Function definition with default value for the country
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city("Reykjavik")  # Default country (Iceland)
describe_city("Paris", "France")  # Custom country (France)
describe_city("New York", "USA")  # Custom country (USA)

# 8.6 EXPLAIN THIS>>>
# Function definition that returns the formatted string
def city_country(city, country):
    return f"{city}, {country}"

# Calling the function with three city-country pairs and printing the returned values
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("New York", "USA"))

# 8.7
# Function definition that builds the album dictionary
def make_album(artist, title, num_songs=None):
    # Create the dictionary
    album = {
        'artist': artist,
        'title': title
    }
    
    # If num_songs is provided, add it to the dictionary
    if num_songs:
        album['num_songs'] = num_songs
    
    return album

# Calling the function to make three albums, including one with a number of songs
album1 = make_album("Adele", "21")
album2 = make_album("The Beatles", "Abbey Road", 17)
album3 = make_album("Taylor Swift", "1989", 13)

# Printing the albums to show the dictionary results
print(album1)
print(album2)
print(album3)

# 8.8
# Function definition (same as in 8-7)
def make_album(artist, title, num_songs=None):
    album = {
        'artist': artist,
        'title': title
    }
    
    if num_songs:
        album['num_songs'] = num_songs
    
    return album

# While loop for user input
while True:
    print("\nEnter album details:")
    artist = input("Artist (or 'quit' to exit): ")
    
    # Break the loop if the user wants to quit
    if artist.lower() == 'quit':
        break
    
    title = input("Album Title: ")
    
    # Ask for the number of songs (optional)
    num_songs_input = input("Number of Songs (or press Enter to skip): ")
    
    # Check if number of songs is provided
    if num_songs_input:
        try:
            num_songs = int(num_songs_input)  # Convert to an integer
        except ValueError:
            print("Please enter a valid number for songs.")
            continue
    else:
        num_songs = None
    
    # Create the album dictionary using the user's input
    album = make_album(artist, title, num_songs)
    
    # Print the album information
    print("\nAlbum information:", album)

# 8.9
# Function to display messages
# def show_messages(messages):
#     for message in messages:
#         print(message)

# List of messages
# messages = ["Hello!", "How are you?", "Have a great day!", "See you soon!"]

# Calling the function to show messages
# show_messages(messages)

# 8.10
# Function to send messages
# def send_messages(messages):
#     sent_messages = []
#     while messages:
#         message = messages.pop()
        # print(message)  # Print the message
        # sent_messages.append(message)  # Move the message to the sent list
    # return sent_messages

# Original list of messages
# messages = ["Hello!", "How are you?", "Have a great day!", "See you soon!"]

# Calling the function and storing the result in sent_messages
# sent_messages = send_messages(messages)

# Printing both lists
# print("\nSent Messages:", sent_messages)
# print("Original Messages after sending:", messages)

# 8.11
# Function to send messages (same as in 8-10)
# def send_messages(messages):
#     sent_messages = []
#     while messages:
#         message = messages.pop()
#         print(message)  # Print the message
#         sent_messages.append(message)  # Move the message to the sent list
#     return sent_messages

# Original list of messages
# messages = ["Hello!", "How are you?", "Have a great day!", "See you soon!"]

# # Making a copy of the list before calling send_messages
# messages_copy = messages[:]
# # Calling the function with the copy of the list
# sent_messages = send_messages(messages_copy)

# # Printing both lists
# print("\nSent Messages:", sent_messages)
# print("Original Messages after sending:", messages)

# 8.12
# Function that accepts a list of sandwich items and prints the sandwich order
# def make_sandwich(*items):
#     print("\nMaking a sandwich with the following ingredients:")
#     for item in items:
#         print(f"- {item}")
#     print("Your sandwich is ready!")

# Calling the function with different numbers of arguments
# make_sandwich("lettuce", "tomato", "cheese")
# make_sandwich("turkey", "bacon")
# make_sandwich("peanut butter", "jelly")

# 8.13
# Function to build a user profile
# def build_profile(first_name, last_name, **user_info):
#     profile = {}
#     profile['first_name'] = first_name
#     profile['last_name'] = last_name
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile

# # Calling the function with my details
# my_profile = build_profile("John", "Doe", age=30, occupation="Software Engineer", location="New York")
# print(my_profile)

# 8.14 EXPLAIN THIS>>>
# Function to store car information
def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Calling the function with manufacturer, model, and additional features
car = make_car('Subaru', 'Outback', color='blue', tow_package=True)
print(car)

# 8.15 EXPLAIN THIS>>>
# Importing functions from printing_functions.py
from printing_functions import print_models, show_printed_models

# List of unprinted models and printed models
unprinted_models = ['Model A', 'Model B', 'Model C']
printed_models = []

# Using the imported functions
print_models(unprinted_models, printed_models)
show_printed_models(printed_models)

# 8.16 
# Method 1: Import the entire module
# import greetings
# greetings.greet("Alice")

# # Method 2: Import only the function
# from greetings import greet
# greet("Bob")

# # Method 3: Import the function with an alias
# from greetings import greet as gr
# gr("Charlie")

# # Method 4: Import the module with an alias
# import greetings as gr
# gr.greet("Dave")

# # Method 5: Import all functions (not recommended for large modules)
# from greetings import *
# greet("Eve")

# 8.17
# def make_sandwich(*items):
#     """Make a sandwich with the provided items."""
#     print("\nMaking a sandwich with the following ingredients:")
#     for item in items:
#         print(f"- {item}")
#     print("Your sandwich is ready!")

