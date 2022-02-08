#!/usr/bin/env python3
import os

current_dir = os.getcwd() + "/Basic IO Files"
file_path = current_dir + '/test.txt'
# open file
my_file = open(file_path)

# read file
# print(my_file.read())

# put cursor back to starting
# my_file.seek(0)
# print(my_file.read())

# readlines
print(my_file.readlines())

my_file.close()