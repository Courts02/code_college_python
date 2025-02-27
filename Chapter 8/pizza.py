def pizza_oven(*toppings):
    print(f"Here is your {toppings} pizza.")

def pizza_fail(customer):
    print(f"{customer}'s pizza has been burnt...")

# pizza_oven("BBQ", "Cheese", "Pepperoni", "Mushroom")

# def pizza_oven(*toppings):
#     print("Here is your pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# pizza_oven("BBQ", "Cheese", "Pepperoni", "Mushroom")

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     if not toppings:
#         print("- Plain cheese")
#     else:
#         for topping in toppings:
#             print(f"- {topping}")
#     print("Your pizza will be ready shortly. Thank you for your order!")

# print("Welcome to Python Pizza!")
# make_pizza(input("What size pizza do you want?"), input("What toppings would you like?"))
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# make_pizza(18)
# print("We hope you enjoy your meal!")
