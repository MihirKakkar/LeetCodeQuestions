# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.

def maxProfit(prices):
    if len(prices) == 0:
        return 0

    minimumPrice = prices[0]
    maximumProf = 0

    for i in prices:
        if i < minimumPrice:
            minimumProf = i
        elif i - minimumPrice > maximumProf:
            maximumProf = i - minimumPrice

    return maximumProf
