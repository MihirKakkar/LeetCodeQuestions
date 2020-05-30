#number that appears more than n/2 times

def majorityElement(A):

    if len(A) == len(set(A)):
        return False

    else: 
        A.sort()
        return A[len(A)//2]

            
print(majorityElement([1,2,3,4,5]))