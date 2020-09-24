# Implement a Python function that takes a string and returns a string containing every other character from original string

def stringChanger(S):
    #initializing variables and making the string an array so that it can be changed
    arrayS = list(S)
    arrayNewWord = []
    evenCounter = 0

    for i in arrayS:
        evenCounter += 1
        if evenCounter % 2 == 1:
            arrayNewWord.append(i)
    NewWord = ''.join(arrayNewWord)
    return NewWord

print(stringChanger("house"))
