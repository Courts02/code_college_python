
# # stores user's details
# user_profile = {}

# # creates user's profile (remember the "double asterix Arbitrary parameter" purpose (think about keys value pairings))
# def create_account(**profile):
    
#     # this is just making a relation to the above variable.
#     global user_profile
#     user_profile = profile

# # logs the user in
# def my_login():
#     logged_in = False

# while logged_in != True:
#         print("Please Login:")

#         un = input("What is your Username: ")
#         pw = input("What is your Password: ")

#         if un == user_profile["username"] and pw == user_profile["password"]:
#             logged_in = True
#             print(f"Here is your profile:\n{user_profile}")
#         else:
#             print("False entry")
            


# stores user's details
# user_profile = {}

# def create_account(**profile):
    
#     global user_profile
#     user_profile = profile

# # Function to log in
# def my_login():
#     while True:
#         print("Please Login:")
#         un = input("Username: ")
#         pw = input("Password: ")

#         # Check if username and password match (after hashing)
#         if un == user_profile["username"] and (pw.encode()) == user_profile["password"]:
#             print(f"Login successful! Here is your profile:\n{user_profile}")
#             break
#         else:
#             print("Invalid credentials. Please try again.")


# def my_login():
#     logged_in = False

#     while logged_in != True:
#         print("Please Login:")

#         un = input("What is your Username: ")
#         pw = input("What is your Password: ")

#         if un == user_profile["username"] and pw == user_profile["password"]:
#             logged_in = True
#             print(f"Here is your profile:\n{user_profile}")

#             print(f"Hi {user_profile["firstname"]} {user_profile["lastname"]}. \nHow are you doing today.\nHow is the weather at {user_profile["location"]}")
#             break
#         else:
#             print("False entry")
#             continue

user_profile = {}

# creates user's profile (remember the "double asterix Arbitrary parameter" purpose (think about keys value pairings))
def create_account(**profile):
    
    # this is just making a relation to the above variable.
    global user_profile
    user_profile = profile


# logs the user in
def my_login():
    logged_in = False

    while logged_in != True:
        print("Please Login:")

        un = input("What is your Username: ")
        pw = input("What is your Password: ")

        if un == user_profile["username"] and pw == user_profile["password"]:
            logged_in = True
            print(f"Here is your profile:\n{user_profile}")

            print(f"Hi {user_profile["firstname"]} {user_profile["lastname"]}.") 
            print(f"\nHow are you doing today.\nHow is the weather at {user_profile["location"]}")
            break
        else:
            print("False entry")
            continue