# !/bin/sh
export opennebula_version='5.2.1'
export sunstone_dir=./opennebula-${opennebula_version}/src/sunstone
export replace_sunstone_dir=./sunstone
export install_file=./opennebula-${opennebula_version}/install.sh
export replace_opennebula="dasone"
export replace_sunstone="mountfront"

#############################################################
# replace images index in install.sh
#############################################################
for file in ${sunstone_dir}/public/images/*
do
    file_name=${file##*/}
    if [ ${file_name#opennebula} != $file_name ];then
        tmp=${file_name//opennebula/$replace_opennebula}
        new_file_name=${tmp//sunstone/$replace_sunstone}
        #echo $new_file_name
        sed -ip "s/${file_name}/${new_file_name}/g" $install_file
    fi
done
echo " replace images index in install.sh "

#############################################################
# replace sunstone public and views file
#############################################################
rm -rf ${sunstone_dir}/public
rm -rf ${sunstone_dir}/views
cp -r ${replace_sunstone_dir}/public $sunstone_dir
cp -r ${replace_sunstone_dir}/views $sunstone_dir
echo " replace sunstone public and views file"


#############################################################
# replace sunstone etc file
#############################################################
rm -rf ${sunstone_dir}/etc/sunstone-views ${sunstone_dir}/etc/sunstone-views.yaml
cp -r ${replace_sunstone_dir}/etc/* $sunstone_dir/etc/
echo "replace sunstone etc file"

#############################################################
# remove svn files
#############################################################
#find opennebula-${opennebula_version} -type d -name "*.svn*" -exec rm -rf {} \;
#echo "remove svn files"


############################################################
# package src code
############################################################
#tar -zcvf opennebula-${opennebula_version}.tar.gz opennebula-${opennebula_version}
#echo "package src code"


