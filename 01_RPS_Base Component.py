import random


# Functions goes here
def rounds_checker():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
        # If infinite mode is not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue
        return response


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

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played the game before
# If 'yes', show instructions

# Loop for testing purposes

# Ask user for choice and check it's valid
user_choice = check_choice("Choose Rock, Paper, and Scissors (r/p/s): ", rps_list,
                           "Please choose from Rock, Paper, Scissors or type 'xxx' to exit")

# Print out choice for comparison purposes
print()
print("You chose {}".format(user_choice))
print()


# Ask user for # of rounds then loop...
rounds_played = 0
choose_instructions = "Please choose Rock (r), Paper (p), Scissors (s)"

# Ask user for # of rounds, press <enter> for infinite mode
rounds = rounds_checker()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Infinite Mode: Round {}".format(rounds_played + 1)

    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        choose = input(choose_instructions)

    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instructions))

    if choose == "xxx":
        break

    # Rest of the loop / game
    print(f"You chose {choose}")

    rounds_played += 1

# Ask user if they want to see their game history
# If 'yes, show game history

# Show game statistics
