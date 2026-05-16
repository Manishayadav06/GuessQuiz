GuessQuiz
Video Demo: https://youtu.be/gUJkW5xF6UQ
Description:
Hello, This is Harshitha, I made this simple GuessQuiz game which is the combination of guess the number and quiz games. I have merged both games into one file, so you will have the option to select which game you want to play. This is created using basic python, it is in the terminal itself, but in the future i want to implement it in GUI. I have also implemented test_project to test them.

Guess the Number
Quiz
The main idea behind this project was to get better at Python basics – things like loops, conditions, functions, working with files, and handling errors. I wanted to make something fun that people could interact with. Instead of making a bunch of separate games, I put them all into one program. That way, when you start it up, you can just pick whichever game you want to play.

Right now, the project works in the command line. I'm planning to add a visual interface later on, maybe using libraries such as tkinter or pygame, to make it more fun to use.

I also spent time on testing. I made a test_project.py file with Python’s unittest and unittest.mock to fake user input. This let me automatically check parts of the game. For example, I checked if the quiz takes right answers, if bad inputs get handled, and if the game goes as it should. Doing tests helped me learn how to check if code is right, even in little projects like this one.

Purpose of the Project
The main idea behind this project was to strengthen my understanding of Python fundamentals like:

1.Loops
2.Conditions
3.Functions
File handling (reading questions from a CSV file)
4.Error handling (for invalid inputs)
I wanted to create something fun and interactive while practicing coding. Instead of writing separate small games, I combined them into one program that gives the user a menu to choose from.

FEATURES

Number Guessing Game

1.Pick how hard you want it to be (1–3).
2.You get 7 tries.
3.If you're close, I'll give you a hint.
4.I'll tell you if your guess is too high or too low.
Quiz Game

1.The questions come from a CSV file called questions.csv.
2.Players get to pick how many questions they want to answer.
3.You get +10 points for each right answer, but watch out! Wrong answers take away -3.33 points.
4.You have up to 3 shots at each question, and we'll give you a hint if you miss the first couple.
Menu

1.When you start, you pick the game you want.
2.When you're done, you can play again or quitby answer y or n.
Testing
1.Has unittest test cases.
2.Uses mock to pretend to be users and check if the game responds right.
How to Run
1.Clone or download the repository.
2.Make sure you have Python installed.
3.Run the game: in the terminal type python project.py
CONCLUSION: The GuessQuiz project helped me strengthen my Python basics while building an interactive game. By combining a number guessing game and a quiz, I practiced using loops, conditions, functions, and file handling. Adding tests with unittest and mock improved my understanding of debugging and validation. Though it runs in the terminal now, I plan to extend it with a graphical interface using Tkinter or Pygame. Overall, this project was a fun and practical way to improve my coding skills.
