import cv2, time

class WebcamDialog:
    def __init__(self, builder):
        self.builder = builder
        print("Inited AddWebcamDialog")

    # addEducamSpecific actions
    def addWebcamCloseDialog(self, widget):
        self.builder.get_object("webcam_settings_dialog").hide()

    def addWebcamSave(self, widget):
        print("Add webcam save")
        self.addWebcamCloseDialog(widget)

    def previewSource(self, camid):
        cv2.namedWindow('Webcam-Preview', cv2.WINDOW_NORMAL)
        cam = cv2.VideoCapture(3)
        FirstTime = True
        while True:
            ret_val, img = cam.read()
            
            cv2.imshow('Webcam-Preview', img)
            # if cv2.getWindowProperty('Webcam-Preview', 0) >= 0:
            #     break

            if cv2.waitKey(1) == 27: 
                break  # esc to quit
            if cv2.getWindowProperty('Webcam-Preview',cv2.WND_PROP_VISIBLE) < 1:        
                break
            # cv2.resizeWindow('Webcam-Preview', cv2.getWindowImageRect('Webcam-Preview')[2], cv2.getWindowImageRect('Webcam-Preview')[3])
        cv2.destroyAllWindows()


    def addWebcam(self, widget):
        print("ADDING WEBCAM")
        addWebcamWindow = self.builder.get_object("webcam_settings_dialog")

        print("Bind cancel btn")
        # Bind cancel btn
        addWebcamCancelBtn = self.builder.get_object("webcam_settings_cancel_btn")
        addWebcamCancelBtn.connect("clicked", self.addWebcamCloseDialog)

        # Bind save btn
        addWebcamCancelBtn = self.builder.get_object("webcam_settings_save_btn")
        addWebcamCancelBtn.connect("clicked", self.addWebcamSave)

        # Bind preview btn
        webcamPreviewBtn = self.builder.get_object("preview-webcam-source")
        webcamPreviewBtn.connect("clicked", self.previewSource)

        # Set char limit
        ipInputBox = self.builder.get_object("webcam_settings_dialog_ip_input")
        # ipInputBox.set_max_length(12)
        
        addWebcamWindow.show()
    