# Guess a Number
from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Functions
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def check_answers(guess, answer):
    global turns
    if guess > answer:
        print("the actual number is too low")
        turns -= 1
    elif guess < answer:
        print("the actual number is too high")
        turns -= 1
    else:
        print("the actual number and the guessed number is same.\n You win!")


print(logo)
# print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")

turns = set_difficulty()
print(f"U have {turns} attempts")

answer = random.randint(1, 100)
guess = 0
while guess != answer:
    print(f"U have {turns} turns remaining")
    guess = input("make a guess\n")
    check_answers(int(guess), answer)
    if turns == 0:
        print("U ran out of turns. U lose")
        break
