#!/bin/bash
echo "----"
echo "ffmpeg -stream_loop -1  $1  $2  $3  $4 -filter_complex"
echo "===="
ffmpeg -stream_loop -1  $1  $2  $3  $4 -filter_complex \
    "
		nullsrc=size=1920x1080 [base];
		[0:v] setpts=PTS-STARTPTS, scale=960x540 [upperleft];
		[1:v] setpts=PTS-STARTPTS, scale=960x540 [upperright];
		[2:v] setpts=PTS-STARTPTS, scale=960x540 [lowerleft];
		[3:v] setpts=PTS-STARTPTS, scale=960x540 [lowerright];
		[base][upperleft] overlay=shortest=1:format=yuv444 [tmp1];
		[tmp1][upperright] overlay=shortest=1:x=960:format=yuv444 [tmp2];
		[tmp2][lowerleft] overlay=shortest=1:y=540:format=yuv444 [tmp3];
		[tmp3][lowerright] overlay=shortest=1:x=960:y=540:format=yuv444
	"\
     -threads 0 -pix_fmt yuyv422 -f v4l2  "/dev/video2"



#### Workling prototpye

# ffmpeg -stream_loop -1  -f x11grab -r 25 -s 1920x1080 -i :1  -i ./resources/video.avi -i ./resources/video.avi -i ./resources/video.avi -filter_complex \
#     "
# 		nullsrc=size=1920x1080 [base];
# 		[0:v] setpts=PTS-STARTPTS, scale=960x540 [upperleft];
# 		[1:v] setpts=PTS-STARTPTS, scale=960x540 [upperright];
# 		[2:v] setpts=PTS-STARTPTS, scale=960x540 [lowerleft];
# 		[3:v] setpts=PTS-STARTPTS, scale=960x540 [lowerright];
# 		[base][upperleft] overlay=shortest=1:format=yuv444 [tmp1];
# 		[tmp1][upperright] overlay=shortest=1:x=960:format=yuv444 [tmp2];
# 		[tmp2][lowerleft] overlay=shortest=1:y=540:format=yuv444 [tmp3];
# 		[tmp3][lowerright] overlay=shortest=1:x=960:y=540:format=yuv444
# 	"\
#      -threads 0 -pix_fmt yuyv422 -f v4l2  "/dev/video2"

