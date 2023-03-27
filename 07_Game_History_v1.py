game_history = []

rounds_played = 5
rounds_lost = 0
rounds_drawn = 0

for item in range(0, 5):
    result = input("choose result: ")

    outcome = f"Round {item}: {result}"

    if result == "tie":
        rounds_drawn += 1

    elif result == "lost":
        rounds_lost += 1

    game_history.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate Game Stats **** #
win_percentage = rounds_won / rounds_played * 100
loss_percentage = rounds_lost / rounds_played * 100
draw_percentage = rounds_drawn / rounds_played * 100

print()
print("***** Game History *****")

for game in game_history:
    print(game)

print()
print("***** Game Summary *****")
print(f"Won: {rounds_won} ({win_percentage:.0f}%) \nDrawn: {rounds_drawn} ({draw_percentage:.0f}%) \n"
      f"Lost: {rounds_lost} ({loss_percentage:.0f}%)")
