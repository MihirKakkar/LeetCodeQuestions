# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
def replaceElements(arr):
    for i in arr:
        if arr[i+1] > arr[i]:
            arr[i+1] = arr[i] and arr[i] = arr[i+1]
            arr[:-1] = -1
            
