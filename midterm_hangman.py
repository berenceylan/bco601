# Beren İlkim Ceylan
# bceylanues@gmail.com
# @berenceylan

import turtle
from random import randint

def drawSnow(wrongCount):
    # set up our stage or canvas
    turtle.setup(600, 600, 0, 0)
    image = "snowman.gif"
    screen = turtle.Screen()
    screen.bgpic(image)

    t = turtle.Pen()
    t.speed(2)
    t.penup()

    # Eye1
    if wrongCount == 1:
        t.goto(30,20)
        t.pendown()
        t.circle(10)
        t.penup()

    # Eye2
    elif wrongCount == 2:
        t.goto(80, 20)
        t.pendown()
        t.circle(10)

    # Nose
    elif wrongCount == 3:
        t.goto(30, -10)
        t.pendown()
        t.left(45)
        t.forward(40)
        t.right(135)
        t.forward(56.56)
        t.right(135)
        t.forward(40)

    #Mouth
    elif wrongCount == 4:
        t.speed(10)
        t.right(90)
        t.pendown()
        for x in range(180):
            t.forward(1)
            t.left(1)
        t.speed(2)

    # Hand1
    elif wrongCount == 5:
        t.goto(0,-90)
        t.left(135)
        t.pendown()
        t.forward(100)

    # Hand2
    elif wrongCount == 6:
        t.goto(110, -90)
        t.right(135)
        t.pendown()
        t.backward(100)

    # Buttons
    elif wrongCount == 7:
        t.goto(50,-120)
        t.right(90)
        t.pendown()
        t.circle(10)
        t.penup()
        t.forward(25)
        t.pendown()
        t.circle(10)
        t.penup()
        t.forward(25)
        t.pendown()
        t.circle(10)


    t.penup()
    t.home()


isGameFinished = False
chosenLetters = []
totalAnswers = 0
wrongAnswers = 0
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
            drawSnow(wrongAnswers)

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
            print("Success rate = " + str(100*(totalAnswers-wrongAnswers)/totalAnswers) + "%")
            print("Game is finished!")

game()
