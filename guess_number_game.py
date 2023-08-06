import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    no_of_attempt = 10
elif difficulty == 'hard':
    no_of_attempt = 5

end_game = False
while not end_game and no_of_attempt > 0:
    print(f"You have {no_of_attempt} attempts remaining to guess the number.")
    my_guess = int(input("Make a guess: "))
    if my_guess == number:
        print(f"Bingo! The answer was {number}.")
        end_game = True
    elif my_guess < number:
        print("Too low.")
    elif my_guess > number:
        print("Too high.")

    no_of_attempt -= 1

if not end_game:
    print("You've run out of guess. You lose.")
