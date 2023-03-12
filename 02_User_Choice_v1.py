# Functions go here...
def check_choice(question):
    while True:
        response = input(question).lower()

        if response == "rock" or response == "r":
            return "rock"

        elif response == "paper" or response == "p":
            return "paper"

        elif response == "scissors" or response == "s":
            return "scissors"

        else:
            print("Please answer yes / no")


# Main Routine goes here
user_choice = check_choice("Choose between Rock, Paper, and Scissors: ")

print()
print("You chose {}".format(user_choice))
print()
# Ask user for choice and check it's valid


# Print out choice for comparison purposes

