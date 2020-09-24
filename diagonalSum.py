# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the 
# secondary diagonal that are not part of the primary diagonal.

def diagonalSum(mat):

    lenY = len(mat)
    finalSum = 0

    #Even length matrix case
    for i in range(lenY):
        finalSum += mat[i][i]
        if lenY > 1:
            finalSum += mat[i][lenY - 1 - i]

    #Removing middle if odd length matrix that is not 1
    if lenY % 2 > 0 and lenY > 1:
        finalSum -= mat[(lenY - 1)// 2][(lenY - 1) // 2]

    return finalSum, lenY


