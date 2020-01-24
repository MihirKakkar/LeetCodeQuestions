# # Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

def BuddyStrings(A, B):
    if len(A) != len(B):
        return False

        table = {}

        for z in range(len(A)):
            if A[i] != B[i]:
                table[i] = A[i]

            if len(table) == 2:
                i,j = table.keys()
                A = list(A)
                A[i] , A[j] = A[j], A[i]
                return "".join(A) == B
            if len(table) == 0 and A == B and len(A) > len(set(A)):
                return True
            else:
                return False
#Copied from someone to learn hash table use
