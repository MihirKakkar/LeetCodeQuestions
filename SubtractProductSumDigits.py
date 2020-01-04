#Given an integer number n, return the difference between the product of its digits and the sum of its digits.
import math
def subtractProductAndSum(n):
    product = 1
    sum = 0

    while n >= 1:
        val = n % 10
        product *= val
        sum += val
        n = math.floor(n / 10)

    return product - sum

  
