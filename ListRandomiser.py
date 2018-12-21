import random

class ListRandomiser:
    def RandomizeList(list = [], dict = {}, randomizationType = ""):
        if len(list) != 0:
            newlist = list
            random.shuffle(newlist)
            return newlist
        if randomizationType == "first" or randomizationType == "second":
            randomKeys = []
            for key in dict.keys():
                randomKeys.append(key)
            random.shuffle(randomKeys)
            return randomKeys
        if randomizationType == "both":
            randomizeBoth = []
            for key, value in dict.items():
                randomizeBoth.append(key)
                randomizeBoth.append(value)
            random.shuffle(randomizeBoth)
            return randomizeBoth
