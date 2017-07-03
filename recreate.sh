#!/bin/bash
cd $1
grunt requirejs
if [ $? -ne 0 ];then
    exit 177
    else
        service opennebula-sunstone restart
        if [ $? -ne 0 ];then
            exit 178
        fi
fi
