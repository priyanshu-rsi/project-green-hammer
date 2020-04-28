import subprocess
import app.home.stream_helper as SH

class WebCamHelper: 
    def __init__(self, builder):
        self.builder = builder
        self.streamhelper = SH.StreamHelper()
        print("Inited webcamhelper")

    def startWebCam(self):
        print("starting webcam")
        process = subprocess.Popen(['./scripts/startWebcam.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait() # Wait for process to complete.
        for line in process.stdout.readlines():
            print(line)

    def stopWebCam(self):
        print("Stopping webcam")
        stopCamResult = True
        process = subprocess.Popen(['./scripts/stopWebcam.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait() # Wait for process to complete.
        for line in process.stdout.readlines():
            print(line)
        for line in process.stderr.readlines():
            print(line)
            line = str(line, 'utf-8')
            if ( line.find("Module akvcam is in use") > -1 ):
                stopCamResult = False
        if stopCamResult:
            print("Success in stopping ") 
        else:
            print("Failed in stopping ") 
            
        return stopCamResult

    def startStream(self):
        print("Straring stream")
        self.streamhelper.startStream()
        


    def stopStream(self):
        print("Stopping stream")
        self.streamhelper.stopStream()