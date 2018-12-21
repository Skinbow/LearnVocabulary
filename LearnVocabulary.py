#
#  LearnVocabulary.py
#  LearnVocabulary
#
#  Created by Mikhail on 01/04/2018.
#  Copyright © 2018 Mikhail. All rights reserved.
#

import ListRandomiser

def waitContinue():
    input("\nPress Enter to continue...\n")

def waitAnswer():
    input("\nPress Enter to see the answer...\n")

def doAQuestionnary(list = [], dict = {}, randList = [], howToRandomize = ""):
    if len(list) != 0:
        for el in list:
            print(el)
            waitContinue()
        return
    if howToRandomize == "first":
        for key in randList:
            print(key)
            waitAnswer()
            print(dict[key])
            waitContinue()
    if howToRandomize == "second":
        for key in randList:
            print(dict[key])
            waitAnswer()
            print(key)
            waitContinue()
    if howToRandomize == "both":
        for el in randList:
            print(el)
            waitAnswer()
            opp = dict.get(el)
            if opp != None:
                print(opp)
            else:
                for k, v in dict.items():
                    if v == el:
                        print(k)
            waitContinue()

def identifyListType(file):
    beginning = True
    for line in file:
        for char in line:
            if char != "\n" and char != ":":
                beginning = False
            if beginning == False:
                if char == "\n":
                    return "list"
                if char == ":":
                    return "dict"
    return "noList"

def main():
    filename = input("Text filename?\n")
    try:
        file = open(filename, "r")
        text = file.readlines()
        file.close()
    except:
        print("Unable to open file!")
        return -1
    filetype = identifyListType(text)
    if filetype == "list":
        list = []
        element = ""
        for line in text:
            for char in line:
                if char != "\n":
                    element += char
                else:
                    if (len(element) == 0):
                        continue
                    list.append(element)
                    element = ""
        randList = ListRandomiser.ListRandomiser.RandomizeList(list=list)
        print("")
        doAQuestionnary(list=randList)

    elif filetype == "dict":
        dict = {}
        key = ""
        value = ""
        recordingKey = True
        for line in text:
            for char in line:
                if char == ":":
                    recordingKey = False
                if char != "\n":
                    if recordingKey:
                        key += char
                    else:
                        value += char
                else:
                    if (len(key) == 0 or len(value) == 0):
                        key = ""
                        value = ""
                        recordingKey = True
                        continue
                    while key[0] == " ":
                        key = key[1:]
                    while key[-1] == " ":
                        key = key[:-2]
                    while value[0] == " " or value[0] == ":":
                        value = value[1:]
                    while value[-1] == " ":
                        value = value[:-2]
                    dict[key] = value
                    key = ""
                    value = ""
                    recordingKey = True
        howToRandomize = input("How do you want your questionnary to be? first/second/both\n")
        randList = ListRandomiser.ListRandomiser.RandomizeList(dict=dict, randomizationType=howToRandomize)
        print("")
        doAQuestionnary(dict=dict, randList=randList, howToRandomize=howToRandomize)

    else:
        print("Invalid file!")

if __name__ == "__main__":
    main()
