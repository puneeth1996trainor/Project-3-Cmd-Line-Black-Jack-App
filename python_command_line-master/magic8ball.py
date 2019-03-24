# Provide a random answer to a magic 8ball question
import random

# Need a list of answers
answers = ["Yes", "OK", "Dunno", "Nope", "Why are you asking me this?", "Doubtful", "Maybe", "It depends", "Ask later"]

# Need to be able to ask a question
while str(input("Do you have a question for the Magic 8Ball? Yes or No    ")) != 'No':
    str(input("What is your question?    "))
    # Need to return a random answer
    r = answers[random.randint(0, len(answers) - 1)]
    print(r)
else:
    print("Good Bye")

# Do you want to ask another question?
# ---- If yes -> REPEAT
# ---- IF no -> Exit the program