#Removes all of the vowels in a string

def VowelRemover(word):

  vowels = {
  'a', 'e', 'i', 'o', 'u'
  }

  for z in word:
      if z in vowels:
          word.replace(z, "")
          return word
          
