import os,sys
import subprocess
from subprocess import check_call
print("Current Working Directory " , os.getcwd())
euid = os.geteuid() 
if euid != 0:
  raise EnvironmentError("Please run the application as a root/administrator")
  exit()
import subprocess,os

from app.helpers.config_helper import ConfigHelper

class StreamHelper:
    def __init__(self):
        print("Inited StreamHelper")
        self.process = False
        self.Config = ConfigHelper()
        self.PID = 0

    def startStream(self):
        script_dir = os.path.realpath(os.path.dirname(sys.argv[0]))

        screenshare = "-i {script_dir}/resources/video.avi".format(script_dir=script_dir)
        webcamshare = "-i {script_dir}/resources/video.avi".format(script_dir=script_dir)
        educamshare = "-i {script_dir}/resources/video.avi".format(script_dir=script_dir)
        comingsoonshare = "-i {script_dir}/resources/video.avi".format(script_dir=script_dir)
        
        data = self.Config.read("educamConfig")
        if data:
            if len(data["ip"]) > 0:
                if data["active"]:
                    print("EDUCAM IS ACTIVE")
                    educamshare = "-i {ip}".format(ip=data["ip"])

        data = self.Config.read("webCamConfig") 
        if data:
            if len( str(data["camid"]) ) > 0:
                if data["active"]:
                    print("WEBCAM IS ACTIVE")
                    educamshare = "-i /dev/video{id}".format(id=data["camid"])

        data = self.Config.read("screenConfig")
        if data:
            if len( str(data["screenid"]) ) > 0:
                if data["active"]:
                    print("SCREEN IS ACTIVE") 
                    educamshare = "-f x11grab -r 25 -s 1920x1080 -i :{id}".format(id=data["screenid"])
        
        _command = "scripts/ffmpeg/screen-webcam.sh '{screenshare}' '{educamshare}' '{comingsoonshare}' '{webcamshare}'".format(screenshare=screenshare, webcamshare=webcamshare, educamshare=educamshare, comingsoonshare=comingsoonshare)
        script=os.path.join(script_dir, _command)
        self.PID = subprocess.Popen([script], shell=True).pid
        self.process = process
        self.process = True
        process.wait() # Wait for process to complete.
        
    def stopStream(self):
        print("Killing stream")
        os.kill(self.PID, 9)
        os.system("sudo kill -9 $(sudo ps aux | grep ffmpeg | awk '{print $2}');")
        # self.process.terminate()
    