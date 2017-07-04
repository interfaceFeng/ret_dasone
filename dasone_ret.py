#!/usr/bin/python
# -*- coding: utf-8 -*-
# This program make change with items below
# * Remove Opennebula Project annotation
# * Replace variable or class naming OpenNebula Opennebula openNebula
# * Replace variable or class naming Sunstone SunStone (no item naming sunStone)
# * Replace url containing opennebula
# * Remove useless items naming opennebula such as "cmartin@opennebula.org"
#   retain its line
# * Replace dir name and file name containing opennebula
#   modify opennebula in files
# * Replace dir name and file name containing sunstone
#   modify sunstone in files
# * Modify views file for web views such as titles
# * Modify index in dir /etc/one/sunstone_views and file /etc/one/sunstone_views.yaml
#   to show image

# Change replace items in default file replace.yaml or use other conf file with usage below



# Usage:
"""
# Use default yaml file
python dasone_ret.py

# Use specify yaml file
python dasone_ret.py -f [filename]

# Recover init opennebula configure
python dasone_ret.py -rv #
"""

import os
import re
import sys
import yaml
import subprocess


file_yaml_path = os.getcwd() + '/replace.yaml'
file_shell_path1 = os.getcwd() + '/dasone_recover.sh'
file_shell_path2 = os.getcwd() + '/recreate.sh'
sunstone_dir = '/usr/lib/one/sunstone'
sunstone_home = '/usr/lib/one/sunstone/public'
sunstone_view = '/usr/lib/one/sunstone/views'
sunstone_server_file = 'usr/lib/one/sunstone/sunstone-server.rb'
sunstone_view_home = '/etc/one'
replace_items = dict()


def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return_code = p.wait()
    return return_code, stdout, stderr


def copy_dir(dir_path):
    ret = run_cmd('cp -rp ' + dir_path + ' ' + dir_path + '.bak')
    if ret[0] != 0:
        print ("Copy dir " + dir_path + ' error ' + str(ret[2]))
        raise Exception

def recover_dir(dir_path):
    ret1 = run_cmd('rm -rf ' + dir_path)
    if ret1[0] != 0:
        print ("Remove dir " + dir_path + ' error ' + str(ret1[2]))
        raise Exception
    ret2 = run_cmd('cp -rp ' + dir_path + '.bak' + ' ' + dir_path)
    if ret2[0] != 0:
        print ("Recover dir " + dir_path + ' error ' + str(ret2[2]))
        raise Exception

def remove_dir(dir_path):
    ret = run_cmd('rm -rf ' + dir_path)
    if ret[0] != 0:
        print ("Remove dir " + dir_path + ' error ' + str(ret[2]))
        raise Exception

def load_yaml_file(path):
    file_yaml_obj = file(path)
    try:
        replace_items = yaml.load(file_yaml_obj)
        print ('Load file ' + file_yaml_path)
        return replace_items

    finally:
        file_yaml_obj.close()







# Remove Opennebula Project annotation
"""
/* -------------------------------------------------------------------------- */
/* Copyright 2002-2017, OpenNebula Project, OpenNebula Systems                */
/*                                                                            */
/* Licensed under the Apache License, Version 2.0 (the "License"); you may    */
/* not use this file except in compliance with the License. You may obtain    */
/* a copy of the License at                                                   */
/*                                                                            */
/* http://www.apache.org/licenses/LICENSE-2.0                                 */
/*                                                                            */
/* Unless required by applicable law or agreed to in writing, software        */
/* distributed under the License is distributed on an "AS IS" BASIS,          */
/* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   */
/* See the License for the specific language governing permissions and        */
/* limitations under the License.                                             */
/* -------------------------------------------------------------------------- */
"""

"""
{{! -------------------------------------------------------------------------- }}
{{! Copyright 2002-2017, OpenNebula Project, OpenNebula Systems                }}
{{!                                                                            }}
{{! Licensed under the Apache License, Version 2.0 (the "License"); you may    }}
{{! not use this file except in compliance with the License. You may obtain    }}
{{! a copy of the License at                                                   }}
{{!                                                                            }}
{{! http://www.apache.org/licenses/LICENSE-2.0                                 }}
{{!                                                                            }}
{{! Unless required by applicable law or agreed to in writing, software        }}
{{! distributed under the License is distributed on an "AS IS" BASIS,          }}
{{! WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   }}
{{! See the License for the specific language governing permissions and        }}
{{! limitations under the License.                                             }}
{{! -------------------------------------------------------------------------- }}
"""

"""
# Copyright (C) YEAR 2002-2016, OpenNebula Project, OpenNebula Systems
# This file is distributed under the same license as the OpenNebula package.
"""

"""
# -------------------------------------------------------------------------- #
# Copyright 2002-2017, OpenNebula Project, OpenNebula Systems                #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
#--------------------------------------------------------------------------- #
"""

"""
COPYRIGHT_HOLDER="2002-2016, OpenNebula Project, OpenNebula Systems"
"""
# this pattern only in ./locale/generate_messages_pot.sh and a hide file
def remove_opennebula_project_annotation():
    compile_license_list = []
    compile_license_1 = re.compile(r'\/\* --*.*?OpenNebula Project.*?--* \*\/', re.S)
    compile_license_2 = re.compile(r'\{\{\! --*.*?OpenNebula Project.*?--* \}\}', re.S)
    compile_license_3 = re.compile(r'\# Copy.*?OpenNebula Project.*?package\.', re.S)
    compile_license_4 = re.compile(r'\# --*.*?OpenNebula Project.*?--* \#', re.S)
    compile_license_5 = re.compile(r'COPYRIGHT_HOLDER.*?Systems"')
    compile_license_list.append(compile_license_1)
    compile_license_list.append(compile_license_2)
    compile_license_list.append(compile_license_3)
    compile_license_list.append(compile_license_4)
    compile_license_list.append(compile_license_5)

    for parent, dir_names, file_names in os.walk(sunstone_home):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                for compile_license in compile_license_list:
                    search = re.search(compile_license, file_content)
                    if search:
                        file_content = re.sub(compile_license, "", file_content)
                        file_obj.seek(0)
                        file_obj.truncate()
                        file_obj.write(file_content)

            finally:
                file_obj.close()


# Replace OpenNebula
# Replace openNebula
# Replace Opennebula
# bak_2
def replace_opennebula_with_case():
    compile_openNebula = re.compile(r'openNebula')
    compile_Opennebula = re.compile(r'Opennebula')
    compile_OpenNebula = re.compile(r'OpenNebula')
    for parent, dir_names, file_names in os.walk(sunstone_home):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                search = re.search(compile_OpenNebula, file_content)
                if search:
                    file_content = re.sub(compile_OpenNebula, replace_items["OpenNebula"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
                search = re.search(compile_openNebula, file_content)
                if search:
                    file_content = re.sub(compile_openNebula, replace_items["openNebula"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
                search = re.search(compile_Opennebula, file_content)
                if search:
                    file_content = re.sub(compile_Opennebula, replace_items["Opennebula"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
                search = re.search(compile_OpenNebula, file_content)

            finally:
                file_obj.close()


# Replace Sunstone
# Replace SunStone
def replace_sunstone_with_case():
    compile_Sunstone = re.compile(r'Sunstone')
    compile_SunStone = re.compile(r'SunStone')
    # compile_SUNSTONE = re.compile(r'SUNSTONE')
    for parent, dir_names, file_names in os.walk(sunstone_home):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                search = re.search(compile_Sunstone, file_content)
                if search:
                    file_content = re.sub(compile_Sunstone, replace_items["Sunstone"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
                search = re.search(compile_SunStone, file_content)
                if search:
                    file_content = re.sub(compile_SunStone, replace_items["SunStone"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
                # search = re.search(compile_SUNSTONE, file_content)
                # if search:
                #     file_content = re.sub(compile_SUNSTONE, replace_items["SUNSTONE"], file_content)
                #     file_obj.seek(0)
                #     file_obj.truncate()
                #     file_obj.write(file_content)
            finally:
                file_obj.close()

# Replace SUNSTONE
def replace_SUNSTONE():
    compile_SUNSTONE = re.compile(r'SUNSTONE')
    for parent, dir_names, file_names in os.walk(sunstone_dir):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                search = re.search(compile_SUNSTONE, file_content)
                if search:
                    file_content = re.sub(compile_SUNSTONE, replace_items["SUNSTONE"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
            finally:
                file_obj.close()


# Remove SUPPORT module which contain opennebula tag
# This tag only used in sunstone server code
"""
SUPPORT = {
    :zendesk_url => "https://opennebula.zendesk.com/api/v2",
    :custom_field_version => 391130,
    :custom_field_severity => 391197,
    :author_id => 21231023,
    :author_name => "DasOne Support Team",
    :support_subscription => "http://opennebula.systems/support/",
    :account => "http://opennebula.systems/buy/",
    :docs => "http://docs.opennebula.org/5.2/",
    :community => "http://opennebula.org/support/community/",
    :project => "DasOne"
}

"""
def remove_support():
    compile_SUPPORT = re.compile(r'SUPPORT = \{.*?\}', re.S)
    file_obj_tmp = file(sunstone_server_file, 'r+')
    try:
        file_content_tmp = file_obj_tmp.read()
        search = re.search(compile_SUPPORT, file_content_tmp)
        if search:
            re.sub(compile_SUPPORT, "", file_content_tmp)
            file_obj_tmp.seek(0)
            file_obj_tmp.truncate()
            file_obj_tmp.write(file_content_tmp)
    finally:
        file_obj_tmp.close()


# Replace url containing opennebula
def replace_url_opennebula():
    compile_url = re.compile(
        r'https?://[a-zA-Z0-9.?/&=:]*')
    compile_opennebula_url = re.compile(
        r'https?://[a-zA-Z0-9.?/&=:]*opennebula[a-zA-Z0-9.?/&=:]*'
    )

    for parent, dir_names, file_names in os.walk(sunstone_home):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                search = re.findall(compile_url, file_content)
                if len(search) > 0:
                    for url_piece in search:
                        if 'opennebula' in url_piece:
                            file_content = re.sub(compile_opennebula_url, replace_items["url"], file_content)
                            break
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)

            finally:
                file_obj.close()


# Remove useless opennebula, retain its line
# bak_3
"""
"Last-Translator: Carlos Martín <cmartin@opennebula.org>\n"
# Daniel Molina <dmolina@opennebula.org>, 2014
"""
def remove_useless_opennebula():
    compile_opennebula_org = re.compile(
        r'opennebula.org')
    for parent, dir_names, file_names in os.walk(sunstone_home):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                file_obj.seek(0)
                for line_content in file_obj.readlines():
                    search = re.search(compile_opennebula_org, line_content)
                    if search:
                        file_content = file_content.replace(line_content, " ", 1)
                file_obj.seek(0)
                file_obj.truncate()
                file_obj.write(file_content)

            finally:
                file_obj.close()



# Modify dir name containing opennebula
# Modify file name containing opennebula
# Modify opennebula in files
def modify_opennebula():
    compile_with_opennebula = re.compile(r'opennebula')
    for parent, dir_names, file_names in os.walk(sunstone_home):
        for dir_piece in dir_names:
            dir_path = parent + '/' + dir_piece
            search_dir = re.search(compile_with_opennebula, dir_piece)
            if search_dir:
                os.rename(dir_path, dir_path.replace("opennebula", replace_items["opennebula"]))
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                search_file = re.search(compile_with_opennebula, file_piece)
                if search_file:
                    os.rename(file_path, file_path.replace("opennebula", replace_items["opennebula"]))
                file_content = file_obj.read()
                search = re.search(compile_with_opennebula, file_content)
                if search:
                    file_content = re.sub(compile_with_opennebula, replace_items["opennebula"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)

            finally:
                file_obj.close()

# Modify dir name containing sunstone
# Modify file name containing sunstone
# Modify sunstone in files
# Escape SContruct file in public file
# Avoid replace url containing /var/lib/one/sunstone
def modify_sunstone():
    compile_with_sunstone = re.compile(r'sunstone')
    compile_absolute_sunstone = re.compile(r'/usr/lib/one/sunstone/[a-zA-Z0-9.?/&=:_-]*')
    compile_absolute_sunstone_multi = re.compile(
        r'(/usr/lib/one/sunstone/)([a-zA-Z0-9.?/&=:_-]*sunstone[a-zA-Z0-9.?/&=:_-]*)'
    )
    for parent, dir_names, file_names in os.walk(sunstone_home):
        for dir_piece in dir_names:
            dir_path = parent + '/' + dir_piece
            search_dir = re.search(compile_with_sunstone, dir_piece)
            if search_dir:
                os.rename(dir_path, parent + '/' + dir_piece.replace('sunstone', replace_items['sunstone']))
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            # escape this file for rpm pack
            if file_piece == "SConstruct":
                continue
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                file_obj.seek(0)
                search_file = re.search(compile_with_sunstone, file_piece)
                if search_file:
                    os.rename(file_path, parent + '/' + file_piece.replace('sunstone', replace_items['sunstone']))
                for file_line in file_obj.readlines():
                    search_line = re.search(compile_with_sunstone, file_line)
                    if search_line:
                        # print ("search line: " + search_line.group())
                        search_absolute_way = re.search(compile_absolute_sunstone, file_line)
                        if not search_absolute_way:
                            file_content = file_content.replace(file_line, file_line.replace(
                                'sunstone', replace_items['sunstone']
                            ))
                        # string contain two or more sunstone (the first is in absolute way)
                        else:
                            search_absolute_way_mutil = re.search(compile_absolute_sunstone_multi, file_line)
                            if search_absolute_way_mutil:
                                file_line_new = re.sub(
                                    compile_absolute_sunstone_multi,
                                    search_absolute_way_mutil.group(1)
                                    + search_absolute_way_mutil.group(2).replace('sunstone', replace_items['sunstone']),
                                    file_line
                                )
                                file_content = file_content.replace(file_line, file_line_new)
                        # Repeat to avoid file line contain both absolute way and sunstone
                        search_absolute_way = re.search(compile_absolute_sunstone, file_line)
                        if not search_absolute_way:
                            # print (file_line.replace(
                            #     'sunstone', replace_items['sunstone']))
                            # print ("search line not absolute:" + search_line.group())
                            file_content = file_content.replace(file_line, file_line.replace(
                                'sunstone', replace_items['sunstone']
                            ))
                file_obj.seek(0)
                file_obj.truncate()
                file_obj.write(file_content)

            finally:
                file_obj.close()

# Sync css class in views dir and replace Opennebula Sunstone in title
def modify_view():
    compile_OpenNebla_Sunstone = re.compile(r'OpenNebula Sunstone')
    compile_sunstone = re.compile(r'sunstone')
    for parent, dir_names, file_names in os.walk(sunstone_view):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                search = re.search(compile_OpenNebla_Sunstone, file_content)
                if search:
                    file_content = re.sub(compile_OpenNebla_Sunstone, replace_items["OpenNebula_Sunstone"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
                search = re.search(compile_sunstone, file_content)
                if search:
                    file_content = re.sub(compile_sunstone, replace_items['sunstone'], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
            finally:
                file_obj.close()



# You must modify index in /etc/one/ to show img
def modify_img_index():
    compile_opennebula_img = re.compile(r'opennebula-5.0')
    for parent, dir_names, file_names in os.walk(sunstone_view_home):
        for file_piece in file_names:
            file_path = parent + '/' + file_piece
            file_obj = file(file_path, 'r+')
            try:
                file_content = file_obj.read()
                search = re.search(compile_opennebula_img, file_content)
                if search:
                    file_content = re.sub(compile_opennebula_img, replace_items["img_title"], file_content)
                    file_obj.seek(0)
                    file_obj.truncate()
                    file_obj.write(file_content)
            finally:
                file_obj.close()







if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] != '-rv':
            print ("Error params: " + sys.argv[1])
            exit(-1)

    if len(sys.argv) > 3:
        print ("Error number of params")
        exit(-1)
    if len(sys.argv) == 3 and sys.argv[1] != '-f':
        print ('Error params: ' + sys.argv[1])
        exit(-1)
    if len(sys.argv) == 3:
        file_yaml_path = sys.argv[2]
    copy_dir(sunstone_home)
    copy_dir(sunstone_view)
    copy_dir(sunstone_view_home)
    replace_items = load_yaml_file(file_yaml_path)

    try:
        if len(sys.argv) == 2 and sys.argv[1] == '-rv':
            return_code, stdout, stderr = run_cmd("%s %s"%(file_shell_path1, sunstone_dir))
            print str(stderr)
            if return_code != 0:
                print ("Cp or rm error: " + str(stderr))
                raise Exception
        else:
            remove_opennebula_project_annotation()
            print ("Remove Opennebula Project annotation")

            # remove_support()
            # print ("Remove support")

            replace_opennebula_with_case()
            print ("Replace OpenNebula")
            print ("Replace openNebula")
            print ("Replace Opennebula")

            replace_sunstone_with_case()
            print ("Replace Sunstone")
            print ("Replace SunStone")

            # replace_SUNSTONE()
            # print ("Replace SUNSTONE")

            replace_url_opennebula()
            print ("Replace url containing opennebula")

            remove_useless_opennebula()
            print ("Remove useless opennebula, retain its line")

            modify_opennebula()
            print ("Modify dir name containing opennebula")
            print ("Modify file name containing opennebula")
            print ("Modify opennebula in files")

            # Repeat modify to avoid some dir after rename whose files cannot be modify
            modify_sunstone()
            modify_sunstone()
            print ("Modify dir name containing sunstone")
            print ("Modify file name containing sunstone")
            print ("Modify sunstone in files")
            #
            modify_view()
            print ("Sync views file")

            modify_img_index()
            print ("Modify index in /etc/one/sunstone_views to show images")




    except Exception as e:
        print (e)
        recover_dir(sunstone_home)
        recover_dir(sunstone_view)
        recover_dir(sunstone_view_home)
        print ("Error happen when recover dir")
    finally:
        # Call shell to create min files and restart opennebula-sunstone service
        return_code, stdout, stderr = run_cmd("%s %s"%(file_shell_path2, sunstone_home))
        print str(stdout)
        if return_code != 0:
            if return_code == 177:
                print ("Grunt min files error: " + str(stderr))
            if return_code == 178:
                print ("Restart opennebula-sunstone error: " + str(stderr))
        remove_dir(sunstone_home + '.bak')
        remove_dir(sunstone_view + '.bak')
        remove_dir(sunstone_view_home + '.bak')












