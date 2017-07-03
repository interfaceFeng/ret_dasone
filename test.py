#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os

sunstone_home = '/usr/lib/one/sunstone/public'
compile_t = re.compile(
    r'[a-zA-Z0-9.?/&=:]*sunstone[a-zA-Z0-9.?/&=:]*', re.S)

number = 0

for parent, dir_names, file_names in os.walk(sunstone_home):
    for file_piece in file_names:
        file_path = parent + '/' + file_piece
        file_obj = file(file_path, 'r+')
        try:
            file222 = file_obj.read()
            file_content = file_obj.readlines()
            print file_content


        finally:
            file_obj.close()