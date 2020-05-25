def removesDuplicate(A):
    
    trueLength = len(A)
    uniqueLength = len(set(A))
    ht = dict()

    if trueLength == uniqueLength:
        return True

    newList = list(dict.fromkeys(A))
    print(newList)

removesDuplicate([1,2,3,4,5,3,4,3,4,5,6,7,8,2,1,2,1,2])