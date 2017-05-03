# Beren İlkim Ceylan
# bceylanues@gmail.com
# @berenceylan

import turtle
from random import randint


screen = turtle.Screen()
image = "snowman.gif"
screen.bgpic(image)

def drawSnow(wrongCount):


    t = turtle.Pen()
    t.speed(2) # draw fast !
    t.pendown() # right s ide of face
    t.circle(20)


isGameFinished = False
chosenLetters = []
totalAnswers = 0
wrongAnswers = 1
wrongLimit = 7

def selectCityName():
    # Randomly selects a city from the given file
    file = "cities.txt"
    f = open(file,'r')
    data = f.readlines() # will append in the list out
    randomIndex = randint(0,len(data)-1)
    city = data[randomIndex]
    
    # Comment out for debug!
    print(city[:-1])
    return city[:-1]

def examineAnswer(answer, word):
    # Checks the answer and prompt accordingly
    global chosenLetters
    global totalAnswers
    global wrongAnswers
    totalAnswers += 1
    if answer in chosenLetters:
        print("Duplicate answer!")
    else:
        chosenLetters.append(answer)
        if answer in word:
            print("There is '"+ answer + "' letter in the word!")
        else:
            print("Nope!")
            wrongAnswers += 1

def userPrompt(answersArray, chosenCity, isFirst):
    # Checks whether the game is finished
    # Prompts the current state of the game
    # Counts answers
    global wrongAnswers
    strToPrompt = ""
    cond = True
    for i in chosenCity:
        if i in answersArray:
            strToPrompt += i + " "
        else:
            strToPrompt += "_ "
            cond = False
    if isFirst:
        print("We have a "+str(len(chosenCity))+" lettered word! Good luck!")
    print(strToPrompt)
    print("Wrong answers: " + str(wrongAnswers) + "/7")
    return cond

def game():
    # Main game loop
    global isGameFinished
    global chosenLetters
    global totalAnswers
    global wrongAnswers
    global wrongLimit
    print("Game is started!")
    chosenCity = selectCityName()
    
    userPrompt([], chosenCity, True)
    while(not isGameFinished):
        answer = input("Enter a letter: ")
        examineAnswer(answer, chosenCity)
        isGameFinished = userPrompt(chosenLetters, chosenCity, False)
        if wrongAnswers >= wrongLimit:
            isGameFinished = True
        if(isGameFinished):
            print("You made "+str(totalAnswers)+" guess!")
            print("Success rate = " + str(100*len(set(chosenCity))/totalAnswers) + "%")
            print("Game is finished!")


game()
