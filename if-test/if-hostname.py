#!/usr/bin/env python3

hostname = input('What is your hostname: ' ) # has user input a hostname
if hostname in 'mtg' or 'MTG':  # should allow any version of mtg to be input
	print('The hostname was found to be: ' + hostname) # acknowledges receipt of hostname input	
	print('The hostname matches expected config') #provides result for if statement
print('Exiting the script') # will advise you the script is ended

