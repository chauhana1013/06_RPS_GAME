# Looks very similar to the token generator for Lucky Unicorn Game
import random

# Main Routine goes here...
choice_options = ["rock", "paper", "scissors"]

for item in range(0, 20):
    computer_choose = random.choice(choice_options)

    if computer_choose == "rock":
        print("rock")

    elif computer_choose == "paper":
        print("paper")

    elif computer_choose == "scissors":
        print("scissors")
