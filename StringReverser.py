#String Reverser

def StringReverser(s):

    l = len(s)
    i = 0
    while i < (l//2):
        s[i],s[l-i-1] = s[l-i-1],s[i]
        i += 1
    return s


print(StringReverser('Hello'))
