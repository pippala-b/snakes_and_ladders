import random
import time

# Snakes and ladders mapping
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

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
    player_pos = 1  # Optional: start at 1
    while player_pos != 100:
        input("Press Enter to roll the dice...")
        player_pos = move_player(player_pos)
        time.sleep(1)
    print("🎉 Congratulations! You won!")
