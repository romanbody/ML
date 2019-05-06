# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:02:33 2019

@author: a621587
"""

import os
import datetime


root_dir = 'd:\\'
working_dir = 'temp'
file_name = 'message.txt'
my_path = os.path.join(root_dir,working_dir)
my_file = os.path.join(root_dir,working_dir,file_name)

my_files = os.listdir(my_path)

for filename in my_files:
        print(filename)

message_file = open(my_file,'a')
message_file.write("\nfiles backed up: "+ str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
message_file.close()
