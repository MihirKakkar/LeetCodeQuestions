# Given two integer arrays startTime and endTime and given an integer queryTime.

# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

def busyStudent(startTime, endTime, queryTime):
    numberOfStudents = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            numberOfStudents += 1
    
    return numberOfStudents

print(busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5))

 