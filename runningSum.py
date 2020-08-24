# Return the running sum of nums.

def runningSum(nums):
    summedArr = []
    x = 0
    for i in nums:
        x += i 
        summedArr.append(x)
    return(summedArr)

print(runningSum([3,1,2,10,1]))
