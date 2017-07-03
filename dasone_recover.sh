#!/bin/bash

rm -rf /etc/one
cp -rp ./one.bak /etc/one
rm -rf $1/public
cp -rp ./public.bak $1/public
rm -rf $1/views
cp -rp ./views.bak $1/views
rm -rf $1/models
cp -rp ./models.bak $1/models
rm -rf $1/sunstone-server.rb
cp -rp ./sunstone-server.rb.bak $1/sunstone-server.rb