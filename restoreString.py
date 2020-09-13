# Given a string s and an integer array indices of the same length.

# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

def restoreString(s, indices):
    
    #error handling
    if len(indices) != len(set(indices)):
         raise ValueError('Must have unique numbers in indices')
    
    #solution
    sList = list(s)
    sListNew = []
    for i in sList:
        for j in indices:
            if sList.index(j) == j:
                sListNew.append(i)
            # print(sList)
            # print(j)

    print(sListNew)

restoreString('dfasdf', [5,4,3,2,1,0])
