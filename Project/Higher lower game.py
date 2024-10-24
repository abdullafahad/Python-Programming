import random


# Function to play the Higher or Lower game
def play_game():
    print("Welcome to the Higher or Lower Game!")

# Random number to start with (between 1 and 100)
    current_number = random.randint(1, 100)
    score = 0

    while True:
        print(f"\nCurrent number: {current_number}")
        guess = input("Will the next number be higher or lower? (type 'higher' or 'lower'): ").lower()

        if guess not in ['higher', 'lower']:
            print("Invalid input. Please type 'higher' or 'lower'.")
            continue

# Generate the next random number
        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")

# Check if the guess is correct
        if (guess == 'higher' and next_number > current_number) or (guess == 'lower' and next_number < current_number):
            print("Good guess! You got it right.")
            score += 1
        else:
            print("Oops! You guessed wrong.")
            break

        current_number = next_number  # Update current number to next number

    print(f"\nGame Over! Your final score is: {score}")


while True:
    play_game()


    '''How to play the game:
1.The program starts with a random number between 1 and 100.
2.The player guesses whether the next number will be higher or lower.
3.The program generates another random number and compares it with the current one.
4.If the player guesses correctly, their score increases and the game continues.
5.The game ends when the player guesses incorrectly.'''
