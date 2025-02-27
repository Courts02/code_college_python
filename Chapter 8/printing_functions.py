# Function to print a list of models
def print_models(unprinted_models, printed_models):
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing model: {current_model}")
        printed_models.append(current_model)

# Function to show all the printed models
def show_printed_models(printed_models):
    print("\nThe following models have been printed:")
    for model in printed_models:
        print(model)
