import random

print("Welcome to the Rock, Paper, Scissors Game!")
print("------------------------------------------\n")

while True:
    choices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choices)
    userChoice = input("Your move! rock, paper, or scissors? \nPick a play: ")
    print(f"User's choice: {userChoice}")
    print(f"Computer's choice: {computerChoice}\n")

    if userChoice == computerChoice:
        print("Draw! Draw! Try play again!")
    elif computerChoice == "rock" and userChoice == "paper":
        print("User WON!")
    elif computerChoice == "paper" and userChoice == "scissors":
        print("User WON!")
    elif computerChoice == "scissors" and userChoice == "rock":
        print("User WON!")
    else:
        print("Computer WON!")
    
    playAgain = input("Play again? (y/n): ")
    if playAgain.lower() != "y":
        print("Thanks for playing! Goodbye!")
        break