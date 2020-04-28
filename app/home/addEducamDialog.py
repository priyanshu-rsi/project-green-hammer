class EducamDialog:
    def __init__(self, builder):
        self.builder = builder
        print("Actions loaded")

    # addEducamSpecific actions
    def addEducamCloseDialog(self, widget):
        self.builder.get_object("educam_settings_dialog").hide()

    def addEducam(self, widget):
        print("ADDING EDUCAM")
        addEducamWindow = self.builder.get_object("educam_settings_dialog")

        print("Bind cancel btn")
        # Bind cancel btn
        addEduCamCancelBtn = self.builder.get_object("educam_settings_cancel_btn")
        addEduCamCancelBtn.connect("clicked", self.addEducamCloseDialog)

        # Set char limit
        ipInputBox = self.builder.get_object("educam_settings_dialog_ip_input")
        # ipInputBox.set_max_length(12)
        
        addEducamWindow.show()
    