source_replace="sunstone"
opennebula_tag="5.2.1-1"
home_tmp=`pwd`
build_home="rpmbuild"
echo "%_topdir $home_tmp/rpmbuild" > $HOME/.rpmmacros
rm -rf $build_home
mkdir -p $build_home/{BUILD,SOURCES,SPECS,RPMS,SRPMS}
cp -rp ./sunstone $build_home/SOURCES/
cp -rp opennebula-${opennebula_tag}/src/{50*,build*,proper*,opennebula-5.2.1,xml*} $build_home/SOURCES/
cp -rp replace_rpm_src.sh $build_home/SOURCES/
cp -rp opennebula-${opennebula_tag}/src/centos7.spec $build_home/SPECS/

