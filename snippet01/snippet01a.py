#!/usr/bin/env python3
inet = open('work3.txt', 'r')
inetlist = inet.readlines()

print('\t' + '\t'.join(inetlist))