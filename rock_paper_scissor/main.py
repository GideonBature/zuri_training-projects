import random

# List of Choice
# p for paper
# R for rock
# P for aper
# S for Scissors

# Welcome message

input("Welcome to Rock, Paper, or Scissors! Press Enter to Start. ")

# Enter Loop

gameOptions = ["R", "P", "S"]

    # Take user input

playerChoice = input("Pick 'R' for 'rock', 'P' for 'paper' or 'S' for   'scissors': ").upper()

    # Validate user input

while playerChoice != "R" and playerChoice != "P" and playerChoice != "S":
    playerChoice = input("Invalid Input, Please try again!: ").upper()

    # Take Computer input

computerChoice = random.choice(gameOptions)

    # 

while computerChoice == playerChoice:
    playerChoice = input("It is a Tie, Please try again!: ").upper()

    # Display the computer and player input
print("Player: ", playerChoice)
print("CPU: ", computerChoice)

    # Check both players' moves and print out the winner

if playerChoice == "R":
    
    if computerChoice == "R":
        print("It is a Tie!")
    elif computerChoice == "P":
        print("Player Lost")
    elif computerChoice == "S":
        print("Player Wins!")
elif playerChoice == "P":
    if computerChoice == "P":
        print("It is a Tie!")
        
        playerChoice = input("It is a Tie, Press Enter to try again!: ").upper()
    elif computerChoice == "S":
        print("Player Lost")
    elif computerChoice == "R":
        print("Player Wins!")
elif playerChoice == "S":
    if computerChoice == "S":
        print("It is a Tie!")
        playerChoice = input("It is a Tie, Press Enter to try again!: ").upper()
    elif computerChoice == "R":
        print("Player Lost")
    elif computerChoice == "P":
        print("Player Wins!")