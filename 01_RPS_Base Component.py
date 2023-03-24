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
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
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
                return item

        # Output error if item not in list
        print(error)
        print()


# Main Routine goes here


# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]


# Ask user if they have played the game before
# If 'yes', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0


# Ask user for # of rounds, press <enter> for infinite mode
rounds = rounds_checker()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Infinite Mode: Round {rounds_played + 1}"
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        if rounds_played == rounds - 1:
            end_game = "yes"

    print(heading)
    choose_instructions = "Please choose Rock (r), Paper (p), Scissors (s): "
    choose_error = "Please choose Rock (r), Paper (p), Scissors (s) or 'xxx' to end: "

    # Ask user for choice and check it's valid
    user_choice = check_choice(choose_instructions, rps_list, choose_error)

    # Get computer choice
    computer_choice = random.choice(rps_list[:-1])

    # Compare choices
    if user_choice == "rock" and computer_choice == "scissors":
        result = "You won!"

    elif user_choice == "paper" and computer_choice == "rock":
        result = "You won!"

    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You won!"

    elif user_choice == computer_choice:
        result = "Its a tie"

    else:
        result = "You lost (better luck next time)"

    # End game if exit code is typed
    if user_choice == "xxx":
        break

    # Rest of the loop / game
    print()
    print(f"You chose {user_choice} and Computer chose {computer_choice}")
    print(result)
    rounds_played += 1


# Ask user if they want to see their game history
# If 'yes, show game history

# Show game statistics
