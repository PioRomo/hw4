def sort_dictionary(dict):
    newDict = sorted(dict.keys(), key=lambda x:dict[x][1])
    newnewDict = "["
    for name in newDict: 
        newnewDict += "('" + name +"', "+ str(dict[name][0]) + "), "
    newnewDict = newnewDict.rstrip(', ')
    newnewDict += "]"
    res = eval(newnewDict)
    return res
