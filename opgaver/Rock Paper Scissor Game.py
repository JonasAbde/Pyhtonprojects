import random


def get_computer_choice():
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return choices[random.randint(1, 3)]


def get_user_choice():
    while True:
        user_input = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
        if user_input in ["Rock", "Paper", "Scissors"]:
            return user_input
        else:
            print("Invalid choice. Please try again.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Scissors" and computer_choice == "Paper") or \
            (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"


def play_game():
    while True:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "Tie":
            print("It's a tie! Let's play again.")
        else:
            print(f"The winner is: {winner}")
            break


if __name__ == "__main__":
    play_game()
