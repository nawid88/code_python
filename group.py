wins = 0

for num in range(1,7):
    game = input(f"Enter results for game {num} (W/L): ")
    if game.lower() == "w" or game.lower() == "W":
        wins += 1

if wins == 5 or wins == 6:
    placement = "Group 1"
elif wins == 3 or wins == 4:
    placement = "Group 2"
elif wins == 1 or wins == 2:
    placement = "Group 3"
else:
    print("You won 0 games, you have been eliminated")

if wins != 0:
    print(f"Congratulations you won {wins} game(s), you were placed in {placement}")