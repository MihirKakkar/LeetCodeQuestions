# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):

    for x in range(len(nums)):
        y = target - nums[x]
        for z in range(len(nums)):
            if y == nums[z]:
                if x == z:
                    pass
                else:
                    return [x, z]

#tests
print(twoSum([1,2,3,4,5], 7))
    #[1,4]
print(twoSum([3,4], 6))
    #None because same index
