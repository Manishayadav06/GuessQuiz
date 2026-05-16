import csv
import random
import math


def getQuestions(questionsCount):
    with open("questions.csv") as file:
        reader = list(csv.DictReader(file))
        questionList = random.sample(reader, questionsCount)
    return questionList


def play():
    print("----------------------------------------------------------------------------------------------------")
    print("                                                Quiz                                                ")
    print("----------------------------------------------------------------------------------------------------")
    while True:
        try:
            questionsCount = int(input('How many Questions you want to answer? '))
            if 1 <= questionsCount <= 106:
                break
            else:
                print("Not in <<RANGE>>")
        except ValueError:
            print("Must be Integer...")
    questionList = getQuestions(questionsCount)

    totalScore = 0
    maxScore = 10
    incorrectScore = 3.33

    for i in questionList:
        count = 3
        score = 0
        while count:
            print(i['question']+': ', end='')
            correctAnswer = i['answer'].upper().strip()
            answer = input().upper().strip()
            if answer == correctAnswer:
                print('Correct..!!')
                score += maxScore
                break
            else:
                print("Incorrect")
                score -= incorrectScore
                if count == 3:
                    print("Hint 1: Starts with", correctAnswer[0])
                elif count == 2:
                    print("Hint 2: Ends with", correctAnswer[-1])
                else:
                    print(f"Answer is {correctAnswer}")
            count -= 1

        totalScore += score
        print("Current Score:", math.ceil(totalScore))

    print(f"Total Score: {math.ceil(totalScore)}/{questionsCount * 10}")
