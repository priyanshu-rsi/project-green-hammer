import gi
import app.home.addEducamDialog as addEducamDialog
import app.home.webcam_actions as webcamactions
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
        window.show_all()

        # ==== Actions
        educamDialog = addEducamDialog.EducamDialog(builder)
        WebCamActions = webcamactions.WebCamActions(builder)

        # EDUCAM360 button bind
        addEduCamBtn = builder.get_object("add_educam_btn")
        addEduCamBtn.connect("clicked", educamDialog.addEducam)

        # Webcam button bind
        startStopStreamBtn = builder.get_object("start_stop_webcam")
        startStopStreamBtn.connect("clicked", WebCamActions.toggleWebCam)

        # Stream button bind
        startStopStreamBtn = builder.get_object("start_stop_stream")
        startStopStreamBtn.connect("clicked", WebCamActions.toggleStream)
        

        Gtk.main()

    
    

    