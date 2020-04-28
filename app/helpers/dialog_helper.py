class DialogHelper:
    def __init__(self, builder):
        self.builder = builder
        print("Inited DialogHelper")

        self.infoDialog = self.builder.get_object("general_info_dialog")
        self.infoDialogTitle = self.builder.get_object("general_info_title")
        self.infoDialogMessage = self.builder.get_object("general_info_message")
        self.builder.get_object("general_settings_cancel_btn").connect("clicked", self.closeDialog)

    def closeDialog(self, widget):
        self.infoDialog.hide()

    def alert(self, title, message, level=0): # Levels | 0 = Success, 1 = Info, 2 = Warn, 3 = Error
        self.infoDialogTitle.set_label(title)
        self.infoDialogMessage.set_label(message)
        self.infoDialog.show()