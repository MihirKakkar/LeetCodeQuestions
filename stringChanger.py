# Implement a Python function that takes a string and returns a string containing every other character from original string

def stringChanger(S):
    #making the string a 
    arrayS = list(S)
    arrayNewWord = []
    evenCounter = 0
    for i in arrayS:
        evenCounter += 1
        if evenCounter % 2 == 1:
            arrayNewWord.append(i)
    NewWord = ''.join(arrayNewWord)
    return NewWord
    # return arrayS

print(stringChanger("Mihir is the coolest guy ever"))
