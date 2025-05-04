def roll_dice():
    return random.randint(1, 6)

def move_player(position):
    dice = roll_dice()
    print(f"You rolled a {dice}")
    position += dice
    if position > 100:
        position -= dice
    print(f"Moved to {position}")

    if position in snakes:
        print(f"Oh no! Bitten by a snake. Down to {snakes[position]}")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder. Up to {ladders[position]}")
        position = ladders[position]
    return position

def play_game():
    player_pos = 0
    while player_pos != 100:
        input("Press Enter to roll the dice...")
        player_pos = move_player(player_pos)
    print("🎉 Congratulations! You won!")

#end