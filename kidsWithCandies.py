# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

def kidsWithCandies(candies, extraCandies):
    results = []
    for i in candies:
        if i + extraCandies >= max(candies):
            results.append("true")
        else:
            results.append("false")
    
    return results 

print(kidsWithCandies([4,2,1,1,2], 1))
