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


# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

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

    # End game if exit code is typed
    if user_choice == "xxx":
        break

    # Compare choices
    if user_choice == "rock" and computer_choice == "scissors":
        result = "won"

    elif user_choice == "paper" and computer_choice == "rock":
        result = "won"

    elif user_choice == "scissors" and computer_choice == "paper":
        result = "won"

    elif user_choice == computer_choice:
        result = "tie"
        rounds_drawn += 1

    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"

    else:
        feedback = f"{user_choice} vs {computer_choice} - You {result}"

    # Rest of the loop / game
    print()
    print(feedback)
    rounds_played += 1


# Ask user if they want to see their game history
# If 'yes, show game history


# Quick Calculations (STATS)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print("***** End Game Summary *****")
print(f"Won: {rounds_won} \t|\t Lose: {rounds_lost} \t|\t Draw: {rounds_drawn}")
print()
print("Thanks for playing")
