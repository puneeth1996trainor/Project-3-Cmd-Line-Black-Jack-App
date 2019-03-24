# Random number guessing game

import random

# Game picks a random number
answer = random.randint(1, 50)
# The player will have a certain number of guesses
guess_count = range(1, 6) # 5 guesses
print("I am thinking of a number between 1 and 50.")

# Ask you/player what is your guess
for guess_taken in guess_count:
    guess_number = len(guess_count) - guess_taken + 1
    print("You have " + str(guess_number) + " guesses. What is your guess?")
    guess = int(input())
# If guess too high -> tells you that it is too high
    if guess > answer:
        print("Your guess is too high!")
# If guess too low -> tells you that it is too low
    elif guess < answer:
        print("Your guess is too low!")
    else:
        break # Our answer is correct

if guess == answer:
    print("Awesome!!! You guessed the number in " + str(guess_taken) + " guesses. You rock!")
else:
    print("Nope. The number I was thinking about was " + str(answer))

# If guess is equal to the answer -> Congrats
# If don't get the answer then -- Nope message and the game quits
