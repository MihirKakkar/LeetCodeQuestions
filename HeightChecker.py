# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

def heightChecker(heights):
    counter = 0
    for i, z in zip(heights, sorted(heights)):
        if i != z:
            counter += 1
    return counter

print(heightChecker([1,1,4,2,1,3]))
