# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

def removeOuterParenthe(word):
  result = ""
  counter = 0
  for i in word:
      if i == "(" and counter == 0:
          counter += 1
      elif i == ")" and counter == 1:
          counter -= 1
      elif i == "(":
          counter +=1
          result += "("
      else:
          counter -= 1
          result += ")"
  return result

print(removeOuterParenthe("(()()())"))
