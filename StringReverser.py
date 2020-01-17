#String Reverser

def StringReverser(stringinput):
    try:
        stringinput = str(stringinput)
        return stringinput[::-1]
        pass
    except Exception as e:
        print("Invalid input!")
        raise
