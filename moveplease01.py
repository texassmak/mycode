#!/usr/bin/env python3

# The following line will rename a file

import shutil

import os

os.chdir('/home/student/mycode/')

## be careful when moving files because it can easily overwrite a file incorrectly.
shutil.move('raynor.obj', 'ceph_storage/')


## Prompts user for a new name for Kerrigan file
xname = input('What is the new name for kerrigan.obj? ')

## This command actually renames the file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



