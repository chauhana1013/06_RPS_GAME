# Version 3 - checks that response is in a given list

# Functions go here...
def check_choice(question, valid_list, error):

    while True:
        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # Iterates through list and if response is an item
        # In the list (or the first letter of an item),
        # the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return response

        # Output error if item not in list
        print(error)
        print()

# Main Routine goes here


# Lists for checking responses
rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = check_choice("Choose Rock, Paper, and Scissors (r/p/s): ", rps_list,
                               "Please choose from Rock, Paper, Scissors or type 'xxx' to exit")

    # Print out choice for comparison purposes
    print()
    print("You chose {}".format(user_choice))
    print()

