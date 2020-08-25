
def numIdenticalPairs(nums):
    i = 0
    j = 0
    resarray =  []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j] and i != j:
                resarray.append("true")
    numGoodPairs = len(resarray) // 2
    return numGoodPairs
    
print(numIdenticalPairs([1,2,3,1,1,3]))