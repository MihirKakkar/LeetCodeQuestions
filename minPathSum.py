# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

def minPathSum(grid):

    column = len(grid)
    row = len(grid[0])

    for i in range(column):
        for x in range(row):
            if i==0 and x==0:
