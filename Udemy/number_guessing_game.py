import random

from art import guess_the_num_logo

print(guess_the_num_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = ""
attempts_left = 0

while difficulty not in ("easy", "hard"):
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':  ")
    if difficulty.lower() == "easy":
        attempts_left = 10
    elif difficulty.lower() == "hard":
        attempts_left = 5
    else:
        print("Invalid difficulty selected!!!")

while attempts_left > 0:
    print(f"You have {attempts_left} remaining to guess the number")
    guess = int(input("Make a guess:  "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")

    attempts_left -= 1
    if attempts_left == 0:
        print("You've ran out of guesses, you lose.")
    else:
        print("Guess again.")
