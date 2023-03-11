def sort_dictionary(dict):
    newDict = sorted(dict.keys(), key=lambda x:dict[x][1])
    return newDict
