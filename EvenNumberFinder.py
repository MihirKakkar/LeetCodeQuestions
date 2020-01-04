def EvenNumberFinder(nums):
  counter = 0
  for i in nums:
    digcount = 0
    while i > 0:
      i = i // 10
      digcount +=1
    if digcount % 2 ==0:
      counter += 1

  print(counter)
  return counter


nums = [1,2,3,4,5,65]
EvenNumberFinder(nums)
