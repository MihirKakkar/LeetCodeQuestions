# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty

def findMedianSortedArrays(nums1, nums2):
    nums3 = sorted(nums1 + nums2)
    if len(nums3) % 2 == 1:
        z = int(len(nums3)/2 - 0.5)
        return nums3[z]
    else:
        lowerNum = int(len(nums3)/2)
        higherNum = int(len(nums3)/2 - 1)
        return (nums3[lowerNum] + nums3[higherNum]) / 2

print(findMedianSortedArrays([1], [2, 3]))
#2
print(findMedianSortedArrays([1, 2], [3, 4]))
#2.5
