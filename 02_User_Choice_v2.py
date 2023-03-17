# Version 2 - error message included when calling function

# Functions go here...
def check_choice(question, error):

    while True:
        response = input(question).lower()

        if response == "rock" or response == "r":
            return "rock"

        elif response == "paper" or response == "p":
            return "paper"

        elif response == "scissors" or response == "s":
            return "scissors"

        elif response == "xxx":
            return response
        else:
            print(error)
            print()


# Main Routine goes here

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = check_choice("Choose Rock, Paper, and Scissors (r/p/s): ",
                               "Please choose from Rock, Paper, Scissors or type 'xxx' to exit")

    # Print out choice for comparison purposes
    print()
    print("You chose {}".format(user_choice))
    print()

