# The game() function in a program lets a user play a game and returns the score as an integer.
# You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score.
# You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random


def game():
    return random.randint(0, 100)


random_score = game()

with open("Hi-score.txt", "r") as f:
    data = f.read()

score = int(data) if data else 0

if random_score > score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(random_score))
    print(f"New High Score: {random_score}")
else:
    print(f"Your Score: {random_score} (Hight score: {score})")
