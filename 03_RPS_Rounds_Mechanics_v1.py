# Function goes here
def rounds_checker():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> " \
                      "or an integer that is more than 0"
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


rounds_played = 0
choose_instructions = "Please choose Rock (r), Paper (p), Scissors (s)"

# Ask user for # of rounds, press <enter> for infinite mode
rounds = rounds_checker()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Infinite Mode: Round {}".format(rounds_played)
        print(heading)
        choose = input("{} or 'xxx' to end: ".format(choose_instructions))
        if choose == "xxx":
            break

    else:
        heading = f"Round {rounds_played + 1} of {rounds}"
        print(heading)
        choose = input(choose_instructions)
        if rounds_played == rounds - 1:
            end_game = "yes"
            