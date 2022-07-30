#! /bin/bash

ping google.com -c 1 2>error.txt| wc -w >~/Documents/check.txt
check=`cat ~/Documents/check.txt`

if [[ $check -eq 36 || $check -eq 35 ]]
then

# updating the latest version of programs
# updating the older system programs
sudo apt update
# upgrading the installed programs
sudo apt upgrade -y 
# checking update in snap
sudo snap refresh
# cleaning the outdated programs after new version installed.
sudo apt autoremove -y
sudo apt autoclean -y
cat << update

------------------------Update the system is completed----------------------

update
else
cat << error
"-----------Network Error...!?-----------"
error
cat error.txt
fi
rm error.txt
rm ~/Documents/check.txt
