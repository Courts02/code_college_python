# 10-4. Guest: Write a program that prompts the user for their name and writes it to a file called guest.txt.

# Prompt the user for their name
name = input("What is your name? ")

# Write the name to a file called guest.txt
with open("guest.txt", "w") as file:
    file.write(name)

print(f"Thank you, {name}! Your name has been written to guest.txt.")

# 10-5. Guest Book: Write a while loop that prompts users for their name and writes each entry to guest_book.txt.

# Open the guest_book.txt file in append mode to add new entries
with open("guest_book.txt", "a") as file:
    while True:
        # Prompt the user for their name
        name = input("What is your name? (Type 'quit' to stop) ")

        if name.lower() == 'quit':
            break  # Exit the loop if the user types 'quit'

        # Write the name to the guest_book.txt file on a new line
        file.write(name + "\n")

print("Thank you for signing the guest book!")

# 10-6. Addition: Program that handles ValueError when non-numeric input is given.

try:
    # Prompt the user for two numbers
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Convert inputs to integers
    num1 = int(num1)
    num2 = int(num2)

    # Add the numbers and print the result
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

except ValueError:
    # Catch the ValueError if inputs are not valid numbers
    print("Oops! That was not a valid number. Please enter valid integers.")

# 10-8. Cats and Dogs: Program to read files and handle FileNotFoundError.

def read_file(file_name):
    try:
        # Try to open and read the file
        with open(file_name, 'r') as file:
            contents = file.read()
            print(f"Contents of {file_name}:")
            print(contents)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Oops! The file {file_name} was not found. Please check the file path.")

# Read the contents of cats.txt
read_file("cats.txt")

# Read the contents of dogs.txt
read_file("dogs.txt")

try:
    #might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    #handle the exception
    print("You can't divide by zero!")
finally:
    #will run no matter what
    print("Execution completed.")
