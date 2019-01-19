#!/bin/bash
echo '123456'| sudo -S iwconfig
sleep 2
sudo modprobe -r iwldvm iwlwifi mac80211
sleep 2
sudo modprobe iwlwifi connector_log=0x1
sleep 2
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode monitor 
sudo ifconfig wlan0 up 
sudo iw wlan0 set channel 64 HT20
sudo ifconfig wlan0 up
sudo linux-80211n-csitool-supplementary/netlink/log_to_file z3_z2_1.dat


