#!/bin/bash

# akvcam -- O
# ffmpeg -i video.webm -s 640x480 -r 30 -f v4l2 -vcodec rawvideo -pix_fmt rgb24 /dev/videoX

## Works perfect
# ffmpeg -f x11grab -r 25 -s 1920x1080 -i :1.0 -vcodec rawvideo -pix_fmt yuv420p -preset ultrafast temp.mkv

ffmpeg -f x11grab -r 25 -s 1920x1080 -i :1.0+1920,1080 -vcodec rawvideo -pix_fmt yuv420p -preset ultrafast -threads 0 -f v4l2  /dev/video2

# -i rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov \


# ffmpeg -f x11grab -r 60 -s 1920x1080 -i :1.0+1920,0 -vcodec rawvideo -pix_fmt yuv420p -threads 0 -f v4l2 -vf 'hflip,scale=640:360' /dev/video3



# ffmpeg -f x11grab -thread_queue_size 64 -video_size 1920x1080 -framerate 30 -i :0 \
#        -f v4l2 -thread_queue_size 64 -video_size 320x180 -framerate 30 -i /dev/video0 \
#        -filter_complex 'overlay=main_w-overlay_w:main_h-overlay_h:format=yuv444' \
#        -vcodec libx264 -preset ultrafast -qp 0 -pix_fmt yuv444p \
#        video.avi
