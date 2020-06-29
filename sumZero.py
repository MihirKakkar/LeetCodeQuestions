# Given an integer n, return any array containing n unique integers such that they add up to 0.

def sumZero(n):
    
    # Defining vars
    result = []
    new = n/2

    for i in range(1, new+1):
    
        # Even case
        result.append(i)
        result.append(-i)
        
    if n % 2 == 1:
        # Odd case
        result.append(0)

    return(result)

print(sumZero(2))