#!/bin/bash
ffmpeg -re -i ./resources/video.avi -map 0:v -f v4l2 /dev/video2