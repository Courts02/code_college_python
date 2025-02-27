# my_name = input("May I have your name please: ")

# def my_function():
#     print(my_name)

# my_function()

# def my_name(user):
#     print(user)

# my_name(input("May I have your name please: "))

# def my_name(user, age):
#     print(f"welcome back {user}! It myst be nice to be {age} years old...")

# my_name(input("May I have your name please:"), input("How old are you: "))

# def describe_city(city, country= "RSA"):
#     print(f"{city} is in {country}")
#     if city =="Pretoria":
#         return f"{city}, ooh so you use a Gautrain.."
#     elif city == "Jhb":
#         return f"{city}, have you seen Vilakazi street"
#     elif city == "Cpt":
#         return f"{city}, have you been to Camps bay"
#     elif city == "Kimberly":
#         return f"{city}, have you seen the big hole of Diamond"
#     else:
#         return f"I dont know {city}"
    
# output = describe_city(input("Enter your city: "))
# print(output)

# first takes one, second takes multiple
def test(first, *second):
    print(f"this is my first arguement: {first}")
    print(f"these are my other arguements: {second}")

test(1, 2, 3, 4, 5)

def test(*first, second):
    print(f"these are my first arguments: {first}")
    print(f"this aisre my other argument: {second}")

test(1, 2, 3, 4, second = 5)
