def maximum69number(num):
    #backwards counter from the right and forwards from left
    strnum = list(map(int, str(num)))
    counter = 0
    for i in range(len(strnum)):
      if i == '6' and counter == 0:
        i == '9'
        counter == counter + 1
        backtoint = [int(i) for i in strnum]
        print(backtoint)
        numb = int(''.join(map(str,backtoint)))
        print(numb)

maximum69number(696969)
