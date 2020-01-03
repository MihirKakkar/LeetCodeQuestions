#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".

def defanger(IP):
    #for all of the digits in the IP, find the '.'
    for i in range (0, len(IP)):
        if i = '.':
            IP.replace('.','[]')

    return IP

print("hry")

defanger(123412.41234)
