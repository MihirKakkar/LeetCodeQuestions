# Balanced strings are those who have equal quantity of 'L' and 'R' characters.

# Given a balanced string s split it in the maximum amount of balanced strings.

# Return the maximum amount of splitted balanced strings.

def balancedStringSplit(s):
  counter = 0
  res = 0
  for i in s:
    if i == 'L':
        counter += 1
    else:
        counter -= 1
    if counter == 0:
        res += 1
  return res

print(balancedStringSplit("RLRRRLLRLL"))
        
