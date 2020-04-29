import gi
import app.home.addEducamDialog as addEducamDialog
import app.home.addWebcamDialog as addWebcamDialog
import app.home.webcam_actions as webcamactions
from app.helpers.config_helper import ConfigHelper
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk, GLib



class UI:
    def __init__(self):

            
        
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path("./theme/juno/gtk-3.0/gtk.css")
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        builder = Gtk.Builder()
        builder.add_from_file("viewpath.glade")

        window = builder.get_object("homeWindow")
        window.connect("destroy", Gtk.main_quit)
        window.show_all()

        ## Actions Binders ##
        educamDialog = addEducamDialog.EducamDialog(builder)
        webcamDialog = addWebcamDialog.WebcamDialog(builder)
        WebCamActions = webcamactions.WebCamActions(builder)

        ## Config Popup buttons ##
        # ADD EDUCAM360 button bind
        addEduCamBtn = builder.get_object("add_educam_btn")
        addEduCamBtn.connect("clicked", educamDialog.addEducam)

        # ADD WEBCAM button bind
        addWebCamBtn = builder.get_object("add_webcam_btn")
        addWebCamBtn.connect("clicked", webcamDialog.addWebcam)

        ## Toggle Buttons ##
        # Toggle EDUCAM360 Usage
        toggleEducamUsageBtn = builder.get_object("educam_source_state")
        toggleEducamUsageBtn.connect("clicked", WebCamActions.toggleEducamUsage)

        # Toggle WEBCAM Usage
        toggleWebcamUsageBtn = builder.get_object("webcam_source_state") 
        toggleWebcamUsageBtn.connect("clicked", WebCamActions.toggleWebcamUsage)

        # Toggle SCREEN Usage
        toggleScreenUsageBtn = builder.get_object("screen_source_state")
        toggleScreenUsageBtn.connect("clicked", WebCamActions.toggleScreenUsage)

        ## Trigger Buttons (Footer) ##
        # Webcam button bind
        startStopStreamBtn = builder.get_object("start_stop_webcam")
        startStopStreamBtn.connect("clicked", WebCamActions.toggleWebCam)

        # Stream button bind
        startStopStreamBtn = builder.get_object("start_stop_stream")
        startStopStreamBtn.connect("clicked", WebCamActions.toggleStream)
        

        Gtk.main()

    
    

    