# MAIN CHALLENGES:
# Create 2 more job positions to select from.
# Make a method that prints out the user instances' details.

# TIPS:
# Extra points if you show team synergy (get as many members to demo different sections)

from sign_up import SignUp as su

class User:

    def __init__(self):
        signup = su()  
        self.user_first_name = signup.first_name
        self.user_second_name = signup.second_name
        self.user_email = signup.email
        self.user_position = signup.position 

    def print_user_details(self):
        print("\n---------------------------")
        print(f"First Name: {self.user_first_name}")
        print(f"Second Name: {self.user_second_name}")
        print(f"Email: {self.user_email}")
        print(f"Position: {self.user_position.position_name}")
        print("-----------------------------\n")

user = User()
user.print_user_details()