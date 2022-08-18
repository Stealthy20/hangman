import random
from words import words

print(
"""
Hello and Welcome to a classic game of hangman.
You will be provided with a random word which lengt is
displayed as -, one - is one letter. 
You have 6 guesses to find the hidden word!
Good Luck!
"""
)

def name():
    """
    Ask the user to input their name
    """
    player_name = input("What is your name?\n")
    print(f"\nHello and Welcome {player_name.capitalize()}\n")
    run_game()
  
def run_game():
    """
    Lets the user start the game
    """
    while True:

        print("Do you wanna start the game?")
        start_game = input('Press "Y" to start and "N" to exit\n').lower()

        if start_game == "y":
            play_game()
            break
        elif start_game == "n":
            end_game()
            break
        else:
            print("\nInvalid input, please press Y or N\n")
            
def random_word(words):
    """
    Generate random word to the game
    """
    word = random.choice(words)
    return word

def play_game():
    print("hej")

def end_game():
    """
    Message shown when player choose to end the game
    """
    print(f"\nThank you for playing! Have a Good Day :)\n")

name ()


