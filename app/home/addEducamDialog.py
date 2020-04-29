import cv2, time
from app.helpers.config_helper import ConfigHelper

class EducamDialog:
    def __init__(self, builder):
        self.builder = builder
        self.Config = ConfigHelper()

        print("Actions loaded")

    def renderConfig(self):
        data = self.Config.read("educamConfig")
        ip = self.builder.get_object("educam_settings_dialog_ip_input") 
        username = self.builder.get_object("educam_settings_dialog_username_input")
        password = self.builder.get_object("educam_settings_dialog_password_input")
        if data:
            self.setText(ip, data["ip"])
            self.setText(username, data["username"])
            self.setText(password, data["password"])
    
    # addEducamSpecific actions
    def addEducamCloseDialog(self, widget):
        self.builder.get_object("educam_settings_dialog").hide()

    def getText(self,textview):
        buffer = textview.get_buffer()
        startIter, endIter = buffer.get_bounds()    
        text = buffer.get_text(startIter, endIter, False) 
        return text

    def setText(self,textview, text):
        buffer = textview.get_buffer()
        buffer.set_text( str(text) )
        startIter, endIter = buffer.get_bounds()    
        text = buffer.set_text(text) 
        return True
    

    def addEducamPreview(self, widget):
        ip = self.builder.get_object("educam_settings_dialog_ip_input") 
        username = self.builder.get_object("educam_settings_dialog_username_input")
        password = self.builder.get_object("educam_settings_dialog_password_input")
        cv2.namedWindow('IPCam-Preview', cv2.WINDOW_NORMAL)
        cam = cv2.VideoCapture( self.getText(ip) )
        FirstTime = True
        while True:
            ret_val, img = cam.read()
            
            cv2.imshow('IPCam-Preview', img)
            if cv2.waitKey(1) == 27: 
                break  # esc to quit
            if cv2.getWindowProperty('IPCam-Preview',cv2.WND_PROP_VISIBLE) < 1:        
                break # Stop when window is closed
        cv2.destroyAllWindows()

    

    def addEducamSave(self, widget):
        ip = self.getText( self.builder.get_object("educam_settings_dialog_ip_input") )
        username = self.getText( self.builder.get_object("educam_settings_dialog_username_input") )
        password = self.getText( self.builder.get_object("educam_settings_dialog_password_input") )
        self.Config.write("educamConfig", {"ip": ip, "username": username, "password": password})
        self.addEducamCloseDialog(widget)

    def addEducam(self, widget):
        print("ADDING EDUCAM")
        self.renderConfig()
        addEducamWindow = self.builder.get_object("educam_settings_dialog")

        print("Bind cancel btn")
        # Bind cancel btn
        addEduCamCancelBtn = self.builder.get_object("educam_settings_cancel_btn")
        addEduCamCancelBtn.connect("clicked", self.addEducamCloseDialog)

        # Bind save btn
        addEduCamCancelBtn = self.builder.get_object("educam_settings_save_btn")
        addEduCamCancelBtn.connect("clicked", self.addEducamSave)

        # Bind preview btn
        addEduCamPreviewBtn = self.builder.get_object("educam_settings_preview_btn")
        addEduCamPreviewBtn.connect("clicked", self.addEducamPreview)

        # Set char limit
        ipInputBox = self.builder.get_object("educam_settings_dialog_ip_input")
        # ipInputBox.set_max_length(12)
        
        addEducamWindow.show()
    