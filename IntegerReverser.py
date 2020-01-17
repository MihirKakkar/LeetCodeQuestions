#Given a 32-bit signed integer, reverse digits of an integer.

def intReverser(num):
    x = str(num)
    negative = '-'
    if x[0] == negative:
        NumberToString = x[1::]
        ReversedNegative = NumberToString[::-1]
        FinalNegative = negative + ReversedNegative
        return FinalNegative

    else:
        NumToString = x[::-1]
        IntNumToString = int(NumToString)
        return IntNumToString

print(intReverser(121234123512353))
        
