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

print(balancedStringSplit("LRLRLRL"))
        
