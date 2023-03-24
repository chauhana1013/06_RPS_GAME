# Shortens up the amount of code used and already uses variables from RPS Base Component
import random

# Main Routine goes here...
rps_list = ["rock", "paper", "scissors", "xxx"]

for item in range(0, 20):
    computer_choice = random.choice(rps_list[:-1])
    print(computer_choice, end="\t")
