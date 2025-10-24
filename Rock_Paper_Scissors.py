import random 

print("Welcome to a game of Rock, Paper, Scissors!")

options = ("rock", "paper", "scissors") # List of possible choices for the game

playing = True

while playing:

    player = None
    computer = random.choice(options) # Computer randomly selects one of the options

    while player not in options: # Loop until the player enters a valid choice
        player = input("Enter your choice (rock, paper, scissors): ").lower() # Get player's choice and convert it to lowercase

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie! Try again.")
    elif player == "rock" and computer == "scissors":
        print("You win! Rock crushes scissors.")
    elif player == "paper" and computer == "rock":
        print("You win! Paper covers rock.")
    elif player == "scissors" and computer == "paper":
        print("You win! Scissors cut paper.")
    else:
        print("You lose! Better luck next time.")

    if not input("Do you want to play again? (y/n): ").lower() == "y": # Check if the player wants to play again
        playing = False

print("Thanks for playing! Goodbye!")