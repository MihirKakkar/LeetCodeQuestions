# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

def BuddyStrings(A, B):
    #making it lower
    A = str(A.lowercase())
    B = str(B.lowercase())
    ArrayA = list(A)
    ArrayB = list(B)

    Alength = len(A)

    if len(A) != len(B):
        return False

    for i in range(0, Alength):
        i += 1
        #initial checker
        if (A[i] == B[i]):
            return True
        else:
            #one swap
            A[i], A[i+1] == A[i+1], A[i]
            if (A[i] == B[i]):
                return True
            else:
                return False
