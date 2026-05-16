import quiz
import guess
import sys


def printMenu():
    print("1. Guess the Number\n2. Quiz")


def choose():
    printMenu()
    while True:
        print("Enter the number of game you like to play: ", end = "")
        try:
            game = int(input())
            if game in [1, 2]:
                break
            else:
                print("Invalid Option Choosen")
        except ValueError:
            print("Enter Valid Answer")
    return game

def GuessQuiz():
    while True:
        game = choose()
        match(game):
            case 1: guess.play()
            case 2: quiz.play()
        while True:
            again = input("Do you wanna play again(y/n): ").lower()
            if again == 'y' or again == 'yes':
                break
            elif again == 'n' or again == 'no':
                print("\n==============SYSTEM EXITED==============\n")
                sys.exit()
            else:
                print("Enter VALID answer (y/n)..!!!")


def main():
    GuessQuiz()

if __name__ == "__main__":
    main()
