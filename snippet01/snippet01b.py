#!/usr/bin/env python3

print("This program can reserve a block of IP addresses, 10 at a time.")
addy = input('Please enter an IPv4 address: ')

def snippet(reserve):
    startIP = addy
    addy_split = addy.split('.')
    addTo = int(addy_split[3]) + 9
    # print(addTo)
    if(addTo >= 255):
        print('Not enough available addresses. Sorry')
    else:
        print('Your reserved IP range is: ' + startIP + ' to ' + addy_split[0] + '.' + addy_split[1] + '.' + addy_split[2] + '.' + str(addTo))

snippet(addy)