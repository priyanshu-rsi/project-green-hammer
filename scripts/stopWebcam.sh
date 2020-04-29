#!/bin/bash
echo "Script stopping webcam"
cd /home/priyanshusharma/Downloads/akvcam-master/src
sudo rmmod akvcam.ko
sudo modprobe -r -f akvcam

