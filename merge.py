def merge(firstList, secondList): 
    len1 = len(firstList)
    len2 = len(secondList)
    i=0
    j=0
    res = []
    
    while i < len1 and j < len2: 
        if firstList[i] < secondList[j]: 
            res.append(firstList[i])
            i+= 1
        else: 
            res.append(secondList[j])
            j+=1
    res = res + firstList[i:] + secondList[j:]
    return res
