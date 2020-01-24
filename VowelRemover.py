#Removes all of the vowels in a string

def VowelRemover(ListWord):

  vowels = {
  'a', 'e', 'i', 'o', 'u'
  }

  for z in ListWord.lower():
    if z in vowels:
        ListWord = ListWord.replace(z, "")

  print(ListWord)

VowelRemover("Heeyeeeeeoeeooooooooooooeeee")
