# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

def diStringMatch(S):
    z = 0
    stringLength = len(S)
    result = [0]

    for i in S:

        if i == "I":
            z = z+1
            result.append(z)

        if i == "D":
            z = z-1
            result.append(z)
            

    return result

print(diStringMatch("IIIIII"))