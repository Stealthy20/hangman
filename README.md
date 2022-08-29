# Hangman
This is a classic Hangman game. In the original game you play this with a friend that choose the hidden word. In this case the computer randomizes a word for you, and it's your job to guess the word before you run out of guesses. 

![Mockup image of the site on diffrent devices](docs/mockup.JPG)

## Live Site
[Heroku](https://stealthy-hangman.herokuapp.com/)
## Repository
[GitHub](https://github.com/Stealthy20/hangman)
## Planning 
### Flowchart
-   Before i started this project i made a flowchart to make sure that i knew what i wanted to code and what the code should do. 
This made me start the project with a plan and a starting point for my game.
I made changes along the way. Espacially to make it better for the user with user stories in mind. But this flow chart was the starting point for the project.

![Image of the flowchart](docs/flowchart.png)

### User stories
- When i started this project i sat down to think about what i needed to do to make this game better, more fun and smoother for the user. I came up with the following things that i wanted to implement to make this happen.
- User Stories
    -   I want the user to input their name and make it come back during the game accomplish the feeling that the game is for the user.
    -   I want the user to know when and why the the input wasn't valid. So i made sure that this was clear in the messages. 
    -   I want the user to see what letters they already guessed so they don't need to remember that to themselves. Would be irritatin with a error message that they already guessed a letter if they can't see the previous guesses. 
    -   I want the user to be able to play again without refreshing the page. So i added the option after the game finishing to type "y" to play again.

## Features 

### Existing Features
-   Intro Screen with rules.
    - Input for the user to input their name.
    - Input to start the game. 

![Image of the intro screen](docs/intro.JPG)

-   The first play screen where the user is met with the hidden word.
    -   A print to tell the user how long the word is.
    -   Input to make their first guess. 

![Image of the first screen of the game](docs/first_game_screen.JPG)

-   A print to let you know if you guess was unvalid, correct or incorrect.
    -   If the guess was unvalid the user is met with a text telling them what input is expected.
    -   If the guess is correct it appers in the hidden word and the guess is added to Guessed Letters
    -   If the guess was incorrect the amount of guesses goes down and the guess is added to Guessed Letters

![Image of the diffrent outcomes from guesses](docs/outcome_guesses.JPG)

-   When game is done the user gets a message that they one or lost and the option to play again.
    -   If the user didnt guess the right word the game let's the user know what the word was. 
    -   If the user says they wanna play again the game randomizes a new word with new guesses. 
    -   If the user says no they are met with a goodbye message. 

![Image of the end of the game](docs/end_game.JPG)

### Future Features
-   I want to add the choice of playing this with a friend. Where one player choose the word and the other tries to guess it. 
-   A score system for two player mode so two players can compete. 

## Testing
I have tested this project as it was built. Every function and parts of bigger functions have been tested seperatly to make sure that they work on their own. 
The project is also tested as a whole game to make sure everything works togheter. It's tested in my own console and in Heroku Terminal. 
This is done by myself and togheter with my mentor to get a extra pairs of eyes. 
I will show some of the bugs i found and how i resolved them here below. 

## Bugs
Here is an example of some of the bugs and problems that i encountered during the making of this project and how i resolved them. 
No remainen bugs should be left in this project. 

### Bug 1
-   I got a error message when the user did a invalid input and the function should run again to make the user do a new input. 
![Image of the error message](docs/bug1.JPG)

### Bug 1 fix 
-   I couldn't call the function withing the function itself. So i wrapped it in a while loop, that is going until a valid input is made.  

![Image of the while loop in the function](docs/bug1fix.JPG)

### Bug 2
-   I got an error message when i tried to reuse the users name in diffrent functions in the game.
![Image of the error message](docs/bug2.JPG)

### Bug 2 fix
-   After alot of research and two contact with the studen support i realised that i forgot to pass the argument everywhere that i call this function. 
![Image of the function that i forgot to pass the argument to](docs/bug2fix.JPG)

### Bug 3
-   I had a problem where the guessed letters didnt appear on the right spot in the word. And sometimes the _ wasn't correctly removed. 
![Image where the letter appears on the wrong place](docs/bug3.JPG)

### Bug 3 fix
-  I had a wrongly added space in the code. Which made the word longer and letters appear on the wrong place. I removed the space and everything worked. Added a print to show how many letters the word is since that became harder to see without the space. 
![Image when the letters appear correctly](docs/bug3fix.JPG)

### Bug 4
-   The user was able to guess the same letter multiple times. And everytime it counted as a new guess. 
![Image of the user beeing able to guess the same letter](docs/bug4.JPG)

### Bug 4 fix
-   I had the wrong keyword in the function. I had a IS insted of IN, which made it compare if it was the same not if the letter was in the list.
![Image of correct error message](docs/bug4fix.JPG)

### Validator Testing
- No errors when i ran the code through pep8online.com validator.

## Deployment
This app was deployed using Code Insitute's mock terminal for Heroku.

### Deploy to Heroku. 
- Go to Heroku.com and create a free account. 
    - Press create a new app. 
    - Go to setting.
    - Add the Python and Node.JS Buildback.
    - It's important that they are in that order.
    - Go back to Deploy and choose Deployment Method Github.
    - Connect your Github.
    - Search for the repository name and press connect.
    - Choose Automatic or Manuall deployment.

### Forking the Guthub Repository.
- You can fork the original GitHub Respository to be able to view or make changes without it affecting the original repository.
  - Go to the GitHub repository.
  - in the top right, press the button named "Fork".
  - You will now have a copy of the repository in your own GitHub. 

### Make a Local Clone
- Go to the GitHub Repository.
  - Click the "Clone" button in the top of the repository.
  - Copy the link.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
  - Press Enter to create your local clone.

## Credits
- Code institute for the deployment terminal
- My mentor Harry Dhillion for great advise and feedback
- Guide used for inspiration and guidence [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w)
- Random Words generated from (https://randomwordgenerator.com/)