from roles import *

# The SignUp class is designed to gather and validate user details and job position selection. 
class SignUp:

    # The __init__ method calls these two methods together to complete the sign-up process.
    def __init__(self):
        self.get_user_details() 
        self.choose_position()

    # get_user_details: Collects the user's first name, last name, and email, & validates that all fields are filled.
    def get_user_details(self):
        self.first_name = input("What is your first name: ").strip().title()
        self.second_name = input("What is your last name: ").strip().title()
        self.email = input("What is your email: ").strip()

        # This code snippet checks if any of the user input fields (first name, last name, or email) are empty, 
        # and if so, it prompts the user to fill in all the fields and then re-collects the inputs by calling the get_user_details method again.
        if self.first_name == "" or self.second_name == "" or self.email == "":
            print("Please fill in all the fields.")
            self.get_user_details()

    # choose_position: Displays available job positions (imported from roles module) and prompts the user to select
    #  a position until a valid choice is made.
    def choose_position(self):
        jobs = {
            "Janitor": janitor,
            "Programmer": programmer,
            "Secretory": secretory,
            "Developer": developer,
            "Manager": manager
        }

        print("\nAvailable Positions:")
        for job in jobs:
            print(f"- {job}")

        while True:
            chosen_role = input("Select your position: ").strip().title()
            if chosen_role in jobs:
                self.position = jobs[chosen_role]
                break
            else:
                print("Invalid choice. Please select a valid position.")