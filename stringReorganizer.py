# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

# If possible, output any possible result.  If not possible, return the empty string.

def stringReorganizer(S):
    
    listS = list(S)
    
    if len(set(listS)) > len(listS):
        print("reorganization needed")
    else:
        print(listS)
print(stringReorganizer('ooofff'))