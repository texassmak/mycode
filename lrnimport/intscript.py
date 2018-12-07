#!/usr/bin/env python3

from subprocess import call
call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")


### Prompt user for interface they want more detail on
interface = input("Enter an interface, like, ens3: ")

## using input, display IPv4 and IPv6 details
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])
