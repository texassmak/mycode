#!/usr/bin/env python3

loginfail = 0   # sets a counter and initializes with 0
loginpass = 0

keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')

## creates alist called keystone_file_lines and each item is a new line read from the file_object
keystone_file_lines=keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
        ## Next 3 parts will print out the IP addresses pulled from the line data. I used another variable to parse specific info from the read line and made that its on file_object.
        tline = keystone_file_lines[i]
        temp, ipaddress = tline.split('from ')
        print('Failed login from: ' + ipaddress)

    elif " -] Authorization failed" in keystone_file_lines[i]:
        loginpass += 1
print('The number of successful log in attempts is ' + str(loginpass))
print('The number of failed log in attempts is ' + str(loginfail)) 


    
