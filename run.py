import random
from words import words

print(
"""
Hello and Welcome to a classic game of hangman.
You will be provided with a random word which is hidden
behind _. If you guess the right letter it will apear in the row.
You have 6 guesses to find the hidden word!
Good Luck!
"""
)


def intro():
    """
    Ask the user to input their name
    """

    while True:
        player_name = input("What is your name?\n")

        if player_name .isalpha():
            print(f"\nHello and Welcome {player_name.capitalize()}\n")
            return player_name.capitalize()
            break
        else:
            print('Invalid input, expected values A-Z')


def start_game():
    """
    Lets the user start the game
    """
    while True:

        print("Do you wanna start the game?")
        start_game = input('Press "Y" to start and "N" to exit\n').lower()

        if start_game == "y":
            play_game(player_name)
            break
        elif start_game == "n":
            end_game(player_name)
            break
        else:
            print("Invalid input, please press Y or N\n")


def random_word():
    """
    Generate random word to the game
    """
    word = random.choice(words)
    return word.upper()


def play_game(player_name):
    """
    Runs the game and handle the guesses from the user
    While loop taken from https://www.youtube.com/watch?v=m4nEnsavl6w
    """
    word = random_word()
    hidden_word = "_ " * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    print(f"Lets Play {player_name}!")
    print(f"You have {tries} tries left!")
    print(f"{hidden_word}\n")
    
    while not guessed and tries > 0:
        guess = input("Make your guess\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess is guessed_letters:
                print("You have already guessed that letter")
            elif guess not in word:
                print(f"{guess} is not in the word, Try Again!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job, {guess}, is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                hidden_word = "".join(word_as_list)
                if "_" not in hidden_word:
                    guessed = True    
        else: 
            print("That's not a valid guess, expected exactly one letter")
        
        print(f"You have {tries} tries left\n")
        print(hidden_word)
        print("\n")
        print(f"Guessed Letters {guessed_letters}")
    if guessed:
        print(f"Congrats {player_name}, you guessed the word! You win!\n")
        start_game()
    else:
        print(f'Sorry {player_name}, you ran out of tries. \ 
           The word was " {word} ". Maybe next time!\n')
        start_game()

def end_game(player_name):
    """
    Message shown when player choose to end the game
    """
    print(f"\nThank you for playing {player_name}! Have a Good Day :)\n")


player_name = intro()
start_game() 


