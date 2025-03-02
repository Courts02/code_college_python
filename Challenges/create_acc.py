# import user_func 
# from user_func import create_account as ca
# from user_func import my_login as ml

# ca(username = input("What would you like your username to be: "),
#                password = input("What would you like your password to be: "), 
#                firstname = input("What is your first name: "),
#                lastname = input("What is your last name: "),
#                location = input("Where do you stay: "))

# ml()

from user_func import create_account as ca
from user_func import my_login as ml

ca(username = input("What would you like your username to be: "),
    password = input("What would you like your password to be: "), 
    firstname = input("What is your first name: "),
    lastname = input("What is your last name: "),
    location = input("Where do you stay: "))

ml()