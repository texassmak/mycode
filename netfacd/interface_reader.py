#!/usr/bin/env python3

import netifaces

#print(netifaces.interfaces())

def inet(netifaces): 
    for i in netifaces.interfaces():
        # print('\n****** IP Address of Interface - ' + i + ' ******')
        try: 
        # print('MAC: ', end='') # This print statement will always print MAC without an end of line
        # print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print(i + ': ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    print()
    mac(netifaces) ### Callout to run the 2nd defined function
    print()

def mac(netifaces): 
    for i in netifaces.interfaces():
        # print('\n****** MAC Address of Interface - ' + i + ' ******')
        try: 
            print(i + ': ', end='') # This print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
          #  print(i + ':' + 'IP: ', end='')  # This print statement will always print IP without an end of line
          #  print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
    
## run
inet(netifaces)

