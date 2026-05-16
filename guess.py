import random


def play():
    print("------------------------------------------------------------------------------------------------")
    print("                                      Number Guessing Game                                      ")
    print("------------------------------------------------------------------------------------------------")

    levels = {
        1: 25,
        2: 50,
        3: 100
    }
    while True:
        try:
            level = int(input(("\nEnter Level (1 - 3): ")))
            print()
            if 1 <= level <= 3:
                break
            else:
                print("\nLevel can only be 1, 2 or 3...!!!\n")
        except ValueError:
            print("\nEnter Valid Number!!!\n")

    maximum = levels[level]

    answer = random.randint(1, maximum)

    print("You have '7' chances to guess correctly!! Good Luck..!!\n")

    count = 7

    while count:
        while True:
            try:
                n = int(input("Guess the Number: "))
                break
            except ValueError:
                print("\nEnter Valid Number..!!!\n")
        if n == answer:
            print("\n***********Guessed Correctly***********\n")
            break
        elif answer - 5 <= n <= answer + 5:
            print("\n<===== High but CLOSE =====>\n" if n >
                  answer else "\n<===== Low but CLOSE =====>\n")
        elif n > answer:
            print("\n<===== Too High =====>\n")
        elif n < answer:
            print("\n<===== Too Low ======>\n")

        count -= 1
