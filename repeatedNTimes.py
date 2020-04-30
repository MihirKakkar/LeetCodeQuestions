# In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.
#
# Return the element repeated N times.


 def repeatedNTimes(A):
    #There is no chance of another repeated number, so the question is really to just find which number repeats

    for i in A:
      if A.count(i) > 1:
        return i
# Test below
# print(repeatedNTimes([1,2,3,3]))
# print(repeatedNTimes([1,1,1,2,3,4]))