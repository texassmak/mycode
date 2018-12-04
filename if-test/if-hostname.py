#!/usr/bin/env python3

hostname = input('What is your hostname: ') # has user input a hostname
if hostname == 'mtg' or hostname == 'MTG' or hostname == 'mTg' or hostname == 'MTg' or hostname == 'mTG' or hostname == 'MtG':  # should allow any version of mtg to be input
    print('The hostname was found to be: ' + hostname) # acknowledges receipt of hostname input	
    print('The hostname matches expected config') #provides result for if statement
else: 
    print('your hostname does not meet expected criteria')
print('Exiting the script') # will advise you the script is ended

