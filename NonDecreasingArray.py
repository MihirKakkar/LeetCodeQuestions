# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

def NonDecreasingArray(arrayyy):
    #counter for number of moves

    for i in arrayyy:
        if arrayyy[i] <= arrayyy[i + 1]:
            return True
            #checks assending order

        else:
            arrayyy[i] == arrayyy[i+1]
            #the single move to make it assending order

            for i in arrayyy:
                if arrayyy[i] <= arrayyy[i + 1]:
                    return arrayyy
                    return True

                else:
                    return False

print(NonDecreasingArray([1, 2, 9, 10, 5]))
