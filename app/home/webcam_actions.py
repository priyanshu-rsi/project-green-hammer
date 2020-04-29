from app.home.webcam_helper import WebCamHelper
from app.helpers.dialog_helper import DialogHelper
from app.helpers.config_helper import ConfigHelper


class WebCamActions:
    def __init__(self, builder):
        self.builder = builder
        print("WebcamActions loaded")

        # Helpers
        self.Config = ConfigHelper()
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
    
    def toggleEducamUsage(self, widget):
        print("Hitting toggleEducamUsage")
        data = self.Config.read("educamConfig")
        if widget.get_active() == True:
            if data:
                if len(data["ip"].strip()) == 0:
                    self.dialoghelper.alert("Error!", "Missing endpoint IP.  \n Please click on 'Configure' button to add an IP")
                    widget.set_active(False)
                else:
                    data["active"] = True
                    self.Config.write("educamConfig", data)
            else:
                self.dialoghelper.alert("Error!", "IPCam/Educam endpoint is not configured yet. \n Please click on 'Configure' button to add an IP")
                widget.set_active(False)
        else:
            if data:
                    data["active"] = False
                    self.Config.write("educamConfig", data)


    def toggleWebcamUsage(self, widget):
        print("Hitting toggleWebcamUsage")
        data = self.Config.read("webCamConfig")
        if widget.get_active() == True:
            if data:
                if len( str(data["camid"]).strip()) == 0:
                    self.dialoghelper.alert("Error!", "No webcam selected.  \n Please click on 'Configure' button to add a webcam")
                    widget.set_active(False)
                else:
                    data["active"] = True
                    self.Config.write("webCamConfig", data)
            else:
                self.dialoghelper.alert("Error!", "Webcam endpoint is not configured yet. \n Please click on 'Configure' button to add a webcam")
                widget.set_active(False)
        else:
            if data:
                    print( len(data) )
                    data["active"] = False
                    self.Config.write("webCamConfig", data)

    def toggleScreenUsage(self, widget):
        print("Hitting toggleScreenUsage")
        data = self.Config.read("screenConfig")
        if widget.get_active() == True:
            if data:
                if len(data["screenid"].strip()) == 0:
                    self.dialoghelper.alert("Error!", "No screen selected.  \n Please click on 'Configure' button to select a screen to share")
                    widget.set_active(False)
                else:
                    data["active"] = True
                    self.Config.write("webCamConfig", data)
            else:
                self.dialoghelper.alert("Error!", "Screen Sharing endpoint is not configured yet. \n Please click on 'Configure' button to add a webcam")
                widget.set_active(False)
        else:
            if data:
                    data["active"] = False
                    self.Config.write("webCamConfig", data)

    
    ## Trigger Buttons (Footer) ##
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