# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

def productExceptSelf(nums):
    counter = 0
    for i in nums:
        counter = counter + 1
        if nums[i] != counter:
            

