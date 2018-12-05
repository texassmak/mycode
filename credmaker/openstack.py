#!/usr/bin/env python3
outFile = open('admin.rc', 'a')

## Ask for OS Auth URL and write it to admin.rc file
print('What is the OS_AUTH_URL?')
osAUTH = input()
print('export OS_AUTH_URL=' + osAUTH, file=outFile)

## Write OS_IDENTITY_API_VERSION=3 out to admin.rc
print('export OS_IDENTITY_API_VERSION=3', file=outFile)

print('What is the OS_PROJECT_NAME?')
osPROJ = input()
print('export OS_PROJECT_NAME=' + osPROJ, file=outFile)

print('What is the OS_PROJECT_DOMAIN_NAME?')
osPROJDOM = input()
print('export OS_PROJECT_DOMAIN_NAME=' + osPROJDOM, file=outFile)

print('What is the OS_USERNAME?')
osUSER = input()
print('export OS_USERNAME=' + osUSER, file=outFile)

print('What is the OS_USER_DOMAIN_NAME?')
osUSERDOM = input()
print('export OS_USER_DOMAIN_NAME=' + osUSERDOM, file=outFile)

print('What is the OS_PASSWORD?')
osPASS = input()
print('export OS_PASSWORD=' + osPASS, file=outFile)

outFile.close

