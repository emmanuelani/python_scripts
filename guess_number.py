# This is a simple project ia about guessing a secret number that the computer would generate
# We will first have to import random module for generating the random number

import random

# Defining the guess function
def guess():
    x = int(input("Choose a number greater than 100: "))
    # assert x < 5 or x > 20, "Choose a number between 5 and 20"
     # Raising an error when x is lower than 5 or greater than 20
    if x <= 100:
        raise ValueError('x is lesser than 100')
    # elif x > 50:
    #     raise ValueError('x is greater than 50')
    # Raising an error when x is not an integer
    assert isinstance(x, int), "Argument should be an integer"
    random_number = random.randint(1, x) # Picking a random number
    print(random_number)
    # print(random_number)
    guess = 0 # Initializing a guess variable that will be used in the while loop
    no_of_trials = 3

    while guess != random_number:
        # Getting the guess input from the user
        guess = int(input(f"Guess a number between 1 and {x}: "))
        # Ensuring that the user only input integers as the guess value
        assert isinstance(guess, int), "Guess should be an integer"
        if no_of_trials == 1:
            print(f"You have no trials left. Try again")
            break
        if guess > random_number:
            no_of_trials -= 1
            print(f"You have {no_of_trials} trials left")
            print(f"Aim lower, {guess} is higher than number")
            
        elif guess < random_number:
            no_of_trials -= 1
            print(f"You have {no_of_trials} trials left")
            print(f"Aim higher, {guess} is lower than number")
        else:
            print("Correct! You guessed the correct number")
        

if __name__ == '__main__':
    guess()