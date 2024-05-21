import random

def getRandomNumber():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def getUserGuess():
    """Prompt the user for a guess and return it as an integer."""
    return int(input("Enter your guess (1-100): "))

def checkNumber(guess, target):
    """Compare the guess with the target number."""
    if guess < target:
        return "higher"
    elif guess > target:
        return "lower"
    else:
        return "equal"

def main():
    target = getRandomNumber()
    guess_count = 0
    while True:
        guess = getUserGuess()
        guess_count += 1
        result = checkNumber(guess, target)
        if result == "equal":
            print(f"Congratulations! You guessed the number in {guess_count} tries. Your score is {guess_count}.")
            break
        else:
            print(f"Your guess is {result}. Try again.")

# Uncomment the following line to run the program
main()
