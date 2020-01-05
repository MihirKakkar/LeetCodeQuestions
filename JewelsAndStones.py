#You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
#Each character in S is a type of stone you have.
#You want to know how many of the stones you have are also jewels.

def numJewelsInStones(J, S):

    counter = 0
    for i in J:
      counter+=S.count(i)
    return counter

print(numJewelsInStones("fadSDWWWWWDFGSf", "FFGHwwww2345wwwJDGHSFHasSd"))
