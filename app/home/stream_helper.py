import subprocess,os
class StreamHelper:
    def __init__(self):
        print("Inited StreamHelper")
        self.process = False
        self.PID = 0

    def startStream(self):
        self.PID = subprocess.Popen(['./scripts/ffmpeg/screen-videofile.sh'], shell=True).pid
        self.process = process
        # process.wait() # Wait for process to complete.
        
    def stopStream(self):
        print("Killing stream")
        os.kill(self.PID, 9)
        self.process.terminate()
    