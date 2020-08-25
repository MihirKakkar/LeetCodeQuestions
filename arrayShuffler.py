# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def arrayShuffler(nums, n):
    newnums = []
    if len(nums) % 2 == 1:
        raise ValueError('Must be an even sized array')
    for i in range(len(nums)//2):
        newnums.append(nums[i])
        newnums.append(nums[i+n])
    return newnums

print(arrayShuffler([1,2,3,4,5], 2))