import random

n = random.randint(1, 50)
guess = 1
print("Guess the number between 1 to 50")
print("Total guesses you have = 5")

while guess < 6:
    num = int(input())
    if num == n:
        print("You won")
        print("You took ", guess, "guesses to win")
        break
    elif num >= n:
        print("guess a little lower")
    elif num <= n:
        print("guess a little higher")

    guess = guess + 1
    print("Guesses left: ", 6 - guess)
    continue

if guess > 5:
    print("Game Over")
    print(f"Hidden number is {n}")
