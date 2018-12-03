#!/usr/bin/env python3

# This command will import shell utility
import shutil

# This command will import the OS module
import os

# This command forces the Python program to start in stated directory
os.chdir('/home/student/mycode/')

# This will copy one file to another file and/or location
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

# This will copy the entire directory to another location or name as stated
shutil.copytree('5g_research/', '5g_research_backup/')
