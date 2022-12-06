import math as m
import random as r

screenW = 40
mainLoop = True
wordsDict = {"een":"one", "twee":"two", "drie":"three", "vier":"four", "vijf":"five", "zes":"six", "zeven":"seven"}

def main():
    global mainLoop
    global wordsDict
    printMenu()
    option = input("optie? (int) ")

    if option == "8":
        mainLoop = False
    elif option == "1":
        printWordList()
    elif option == "2":
        wordsClear()
    elif option == "3":
        wordChange()
    elif option == "4":
        addWord()
    elif option == "5":
        quiz()
    elif option == "6":
        writeWordsDict()
    elif option == "7":
        loadWordsDict()

def printMenu():
    printBorder("menu")
    menuRow("print woordenlijst", "1")
    menuRow("nieuwe woordenlijst", "2")
    menuRow("verander woord", "3")
    menuRow("woorden toevoegen", "4")
    menuRow("overhoren", "5")
    menuRow("woorden lijst opslaan (.txt)", "6")
    menuRow("woorden lijst laden", "7")
    menuRow("stoppen", "8")
    printBorder("")

def printWordList():
    if len(wordsDict) > 0:
        printBorder("woorden lijst")
        for key in wordsDict:
            wordListRow(key, wordsDict[key])
        printBorder("")
    else:
        printNot("error", "de woordenlijst is leeg")

def wordsClear():
    global wordsDict
    wordsDict = {}
    printNot("woordenlijst", "woordenlijst is geleegd")
        
def wordChange():
    printWordList()
    if input("woord of vertaling veranderen? woord: 1 | vertaling: 2 ") == "1":
        key = input("woord? ")
        newKey = input("nieuw woord? ")
        wordsDict[newKey] = wordsDict.pop(key)
        printNot("verandering", "woord veranderd")
    else:
        key = input("woord (geen vertaling)? ")
        newValue = input("nieuwe vertaling? ")
        wordsDict[key] = newValue
        printNot("verandering", "vertaling veranderd")

def addWord():
    newKey = input("nieuw woord? ")
    newValue = input("nieuwe vertaling? ")
    wordsDict[newKey] = newValue
    printNot("verandering", "nieuw woord toegevoegd")

def quiz():
    global mistakes
    mistakes = 0
    scoreList = []
    if input("1: woord naar vertaling | 2: vertaling naar woord ") == "1":
        quizQuestions = list(wordsDict.keys())
        quizAnswers = list(wordsDict.values())
    else:
        quizQuestions = list(wordsDict.values())
        quizAnswers = list(wordsDict.keys())

    amountQuestions = int(input("hoe vaak? (er zitten " + str(len(quizQuestions)) + " woorden in de lijst) " ))
    for i in range(amountQuestions):
        index = r.randrange(0, len(quizQuestions))
        question(quizQuestions[index], quizAnswers[index])

    printResults(amountQuestions, quizQuestions)

def writeWordsDict():
    f = open(input("naam van nieuw bestand? (bijv: lijst.txt) "), "w")

    for key in wordsDict:
        f.write(key + "=" + wordsDict[key] + "\n")
    
    f.close()

def loadWordsDict():
    global wordsDict
    wordsDict = {}
    if input("lijst laden? dit verwijderd de huidige lijst. ja|nee ") == "ja":
        fileName = input("naam van bestand? (bijv: lijst.txt) ")
        with open(fileName) as f:
            fileData = f.read().split('\n')

    for item in fileData:
        if "=" in item:
            word, translation = item.split('=')
            wordsDict[word] = translation

    printNot("lijst geladen", fileName + " geladen")



def question(question, answer):
    global mistakes
    if input(question + " ") == answer:
        print("goed ")
    else:
        print("fout, het was: " + answer + " ")
        mistakes += 1

def printResults(amountQuestions, quizQuestions):
    printBorder("resultaten")
    printRow("aantal woorden: " + str(len(quizQuestions)))
    printRow("aantal vragen: " + str(amountQuestions))
    printRow("aantal fouten: " + str(mistakes))
    printRow("aantal goed: " + str(amountQuestions-mistakes))
    printRow("precentage goed: %" + str(round((amountQuestions-mistakes)/amountQuestions*100)))
    printBorder("")

def printNot(title, message):
    printBorder(title)
    printRow(message)
    printBorder("")

def printRow(s):
    print(("| " + "{:" + str(screenW-1)+ "}").format(s) + "|")

def wordListRow(word, translation):
    space =  screenW-3-round((len(word)+len(translation))/2)
    print(("| " + word + ": {:" + str(space)+ "}").format(translation) + "|")    

def menuRow(word, number):
    print(("| " + number + ": {:" + str(screenW-4)+ "}").format(word) + "|")

def printBorder(word):
    if word == "":
        print("+" + screenW*"-" + "+")
    else:
        print("+" + int(screenW/2-len(word)/2-1)*"-" + "=" + word + "=" + int(screenW/2-len(word)/2-1 + len(word)%2)*"-" + "+")


    

while mainLoop:
    main()