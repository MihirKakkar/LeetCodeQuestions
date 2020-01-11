#convert roman numerals to integers

def roman_to_int(roman):

#keep the roman letters positive
    roman = roman.upper()

#a dictionary for all of the numerals
    numerals = {
    'M':1000,
    'D':500,
    'C':100,
    'L':50,
    'X':10,
    'V':5,
    'I':1
    }

#starting sum is 0    
    finalInt = 0

#the meat of the function -> adds up everything in the range of the input
    for i in range(len(roman)):

        #using the dictionary to get values for the inputs
        value = numerals[roman[i]]

        #if the next letter is larger then u have to subtract this one cause thats how roman numerals work
        if i + 1 < len(roman) and numerals[roman[i + 1]] > value:
            finalInt -= value

        else:
           finalInt += value

    return finalInt
