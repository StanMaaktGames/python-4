import math as m
import random as r
screen_w = 40

def main():
    words_dict = {"een":"one", "twee":"two", "drie":"three", "vier":"four", "vijf":"five", "zes":"six", "zeven":"seven"} 
    print_menu()
    while (option := input("optie? (int) ")) != "9":
        if option == "1":
            print_word_list(words_dict)
        elif option == "2":
            words_dict = words_clear()
        elif option == "3":
            word_change(words_dict)
        elif option == "4":
            add_word(words_dict)
        elif option == "5":
            delete_word(words_dict)
        elif option == "6":
            quiz(words_dict)
        elif option == "7":
            write_words_dict(words_dict)
        elif option == "8":
            load_words_dict(words_dict)
        print_menu()

def print_menu():
    print_border("menu")
    menu_row("print woordenlijst", "1")
    menu_row("nieuwe woordenlijst", "2")
    menu_row("verander woord", "3")
    menu_row("woord toevoegen", "4")
    menu_row("woord verwijderen", "5")
    menu_row("overhoren", "6")
    menu_row("woorden lijst opslaan (.txt)", "7")
    menu_row("woorden lijst laden", "8")
    menu_row("stoppen", "9")
    print_border("")

def print_word_list(words_dict):
    if len(words_dict) > 0:
        print_border("woorden lijst")
        for key in words_dict:
            word_list_row(key, words_dict[key])
        print_border("")
    else:
        print_not("error", "de woordenlijst is leeg")

def words_clear():
    print_not("woordenlijst", "woordenlijst is geleegd")
    return {}
        
def word_change(words_dict):
    print_word_list(words_dict)
    if input("woord of vertaling veranderen? woord: 1 | vertaling: 2 ") == "1":
        key = input("woord? ")
        new_key = input("nieuw woord? ")
        words_dict[new_key] = words_dict.pop(key)
        print_not("verandering", "woord veranderd")
    else:
        key = input("woord (geen vertaling)? ")
        new_value = input("nieuwe vertaling? ")
        words_dict[key] = new_value
        print_not("verandering", "vertaling veranderd")

def add_word(words_dict):
    new_key = input("nieuw woord? ")
    new_value = input("nieuwe vertaling? ")
    print_not("verandering", "nieuw woord toegevoegd")
    words_dict[new_key] = new_value

def delete_word(words_dict):
    word = input("welk woord wil je verwijderen? ")
    del words_dict[word]

def quiz(words_dict):
    mistakes = 0
    score_list = []
    amount_questions = int(input("hoe vaak? (er zitten " + str(len(words_dict)) + " woorden in de lijst) " ))
    counter = 0

    if input("1: woord naar vertaling | 2: vertaling naar woord ") == "1":
        while counter < amount_questions:
            for key, value in words_dict.items():
                mistakes = question(key, value, mistakes)
                counter += 1
                if counter == amount_questions:
                    break    
    else:
        while counter < amount_questions:
            for key, value in words_dict.items():
                mistakes = question(value, key, mistakes)
                counter += 1
                if counter == amount_questions:
                    break    

    print_results(amount_questions, words_dict, mistakes)

def write_words_dict(words_dict):
    f = open(input("naam van nieuw bestand? (bijv: lijst.txt) "), "w")

    for key in words_dict:
        f.write(key + "=" + words_dict[key] + "\n")
    
    f.close()

def load_words_dict(words_dict):
    words_dict = {}
    if input("lijst laden? dit verwijderd de huidige lijst. ja|nee ") == "ja":
        file_name = input("naam van bestand? (bijv: lijst.txt) ")
        with open(file_name) as f:
            file_data = f.read().split('\n')

    for item in file_data:
        if "=" in item:
            word, translation = item.split('=')
            words_dict[word] = translation

    print_not("lijst geladen", file_name + " geladen")



def question(question, answer, mistakes):
    if input(question + " ") == answer:
        print("goed ")
    else:
        print("fout, het was: " + answer + " ")
        mistakes += 1
    return mistakes

def print_results(amount_questions, words_dict, mistakes):
    print_border("resultaten")
    print_row("aantal woorden: " + str(len(words_dict)))
    print_row("aantal vragen: " + str(amount_questions))
    print_row("aantal fouten: " + str(mistakes))
    print_row("aantal goed: " + str(amount_questions-mistakes))
    print_row("precentage goed: %" + str(round((amount_questions-mistakes)/amount_questions*100)))
    print_border("")

def print_not(title, message):
    print_border(title)
    print_row(message)
    print_border("")

def print_row(s):
    print(("| " + "{:" + str(screen_w-1)+ "}").format(s) + "|")

def word_list_row(word, translation):
    space =  screen_w-3-round((len(word)+len(translation))/2)
    print(("| " + word + ": {:" + str(space)+ "}").format(translation) + "|")    

def menu_row(word, number):
    print(("| " + number + ": {:" + str(screen_w-4)+ "}").format(word) + "|")

def print_border(word):
    if word == "":
        print("+" + screen_w*"-" + "+")
    else:
        print("+" + int(screen_w/2-len(word)/2-1)*"-" + "=" + word + "=" + int(screen_w/2-len(word)/2-1 + len(word)%2)*"-" + "+")

main()
