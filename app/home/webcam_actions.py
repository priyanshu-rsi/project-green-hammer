from app.home.webcam_helper import WebCamHelper
from app.helpers.dialog_helper import DialogHelper
class WebCamActions:
    def __init__(self, builder):
        self.builder = builder

        # Helpers
        self.webcamhelper = WebCamHelper(builder)
        self.dialoghelper = DialogHelper(builder)

        # States
        self.WebCamState = False
        self.StreamState = False

        # Labels
        self.startWebCam = "Start Webcam"
        self.stopWebCam = "Stop Webcam"

        self.startStream = "Start Stream"
        self.stopStream = "Stop Stream"
        
        

        print("Inited WebCamActions")

    def toggleWebCam(self, widget):
        if self.WebCamState:
            print("Toggeling webcam: OFF")
            state = self.webcamhelper.stopWebCam()
            if state:
                widget.set_label(self.startWebCam)    
                self.WebCamState = False
            else:
                print("ERROR !!")
                self.dialoghelper.alert("Error in stopping webcam", "The webcam is being used. \n Please close the application(s) using it and try again")
        else:
            print("Toggeling webcam:ON")
            self.webcamhelper.startWebCam()
            widget.set_label(self.stopWebCam)
            self.WebCamState = True

    def toggleStream(self, widget):
        if self.StreamState:
            print("Toggeling stream: OFF")
            self.webcamhelper.stopStream()
            widget.set_label(self.startStream)
            self.StreamState = False
        else:
            print("Toggeling stream:ON")

            if not self.WebCamState:
                self.dialoghelper.alert("Error in starting stream", "VIEWpath is not running. Please click on 'Start Webcam' first and try again")
                return False

            self.webcamhelper.startStream()
            widget.set_label(self.stopStream)
            self.StreamState = True