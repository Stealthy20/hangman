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
    name = input("What is your name?\n")
    print(f"Hello and Welcome {name}")
    run_game()


def run_game():
    print("Do you wanna play?")
name ()