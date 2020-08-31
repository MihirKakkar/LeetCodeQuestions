# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

def smallerNumbersThanCurrent(nums):
    # INEFFICIENT SOLUTION: 
    # resultArr = []
    # for i in nums:
    #     numberOfSmaller = 0
    #     for j in nums:
    #         if i > j:
    #             numberOfSmaller += 1
    #     resultArr.append(numberOfSmaller)
            
    # return resultArr

    #NEW SOLUTION
    resultArr = []
    sortedArr = sorted(nums)
    hm = {}
    for i in range(len(sortedArr)):
        if sortedArr[i] not in hm:
            hm[sortedArr[i]] = i
    for i in range(len(nums)):
        resultArr.append(hm[nums[i]])
    return resultArr

print(smallerNumbersThanCurrent([1,4,3,7]))