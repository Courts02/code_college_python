#  How the input() Function Works

# The `input()` function pauses the program, waits for the user to enter text, and stores it in a variable for further use.
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing Clear Prompts

# When using input(), provide a clear prompt to tell the user what information to enter
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# Sometimes you’ll want to write a prompt that’s longer than one line. 
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

# Using int() to Accept Numerical Input
# The `input()` function in Python treats all user input as a string.
age = input("How old are you? ")
age = int(age)
age >= 18

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

number = input("Enter a number, and I'll tell you if it's even or odd: ")

# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# Introducing while Loops
# A `for` loop iterates over a collection, executing code once for each item, while a `while` loop runs as long as a specified condition is true.

# The while Loop in Action
# You can use a while loop to count up through a series of numbers. For example,  
# the following while loop counts from 1 to 5:

current_number = 1
while current_number <= 5:
  print(current_number)
current_number += 1  

# Letting the User Choose When to Quit
# You can make the `parrot.py` program run continuously by placing it inside a `while` loop, using a 
# quit value to stop the loop when the user enters it.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Using a Flag
# In complex programs, like games, multiple events can stop the program. To handle this, you can use a 
# flag variable that signals whether the program should keep running. The program continues as long as the flag 
# is `True` and stops when any event sets the flag to `False`. This simplifies the logic, as the main loop only needs to check the flag.

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to Exit a Loop
# The `break` statement exits a `while` loop immediately, skipping any remaining code in the loop, and 
# gives you control over which code is executed.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Using continue in a Loop
# The `continue` statement skips the current iteration of a loop and returns to the beginning, based 
# on a conditional test. For example, it can be used to print only odd numbers in a loop counting from 1 to 10.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
print(current_number)

# Avoiding Infinite Loops
# Every while loop needs a way to stop running so it won’t continue to run for ever.
# For example, this counting loop should count from 1 to 5:
x = 1
while x <= 5:
    print(x)
#    x += 1
#However, if you accidentally omit the line x += 1, the loop will run forever 

# Using a while Loop with Lists and Dictionaries
# To handle multiple users and data, use lists and dictionaries with `while` loops. 
# Avoid modifying a list inside a `for` loop; instead, use a `while` loop to safely modify the list.

# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
     current_user = unconfirmed_users.pop()
     print(f"Verifying user: {current_user.title()}")
     confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input
# In a `while` loop, you can prompt for multiple inputs each time. For example, a polling program can
# collect a participant's name and response, storing the data in a dictionary to link each response to a user.

responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    # Prompt for the person's name and response.
     name = input("\nWhat is your name? ")
response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary.
responses[name] = response
    # Find out if anyone else is going to take the poll.
repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False
 # Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

    