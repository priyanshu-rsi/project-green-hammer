#!/bin/bash
echo $(pwd)
ls ./resources
ffmpeg -re -i ./resources/video.avi -map 0:v -f v4l2 -vcodec rawvideo -pix_fmt rgb24 "/dev/video$1"