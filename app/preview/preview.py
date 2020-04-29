import gi
import app.home.addEducamDialog as addEducamDialog

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk, GLib

    
class Preview:
    def __init__(self):
        print("Preview inited")

    def UI(self):
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        provider.load_from_path("./theme/juno/gtk-3.0/gtk.css")
        Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

        builder = Gtk.Builder()
        builder.add_from_file("viewpath.glade")

        window = builder.get_object("videoPreviewWindow")
        window.show_all()

        # Bind sources list to combobox
        audioSourcesComboBox = builder.get_object("select_audio_sources")
        
        audioSources = Gtk.CellRenderer
        audioSources.append([1, "Billy Bob"])
        audioSources.append([11, "Billy Bob Junior"])

        audioSourcesComboBox.pack_start(audioSources, False)


        # ==== Actions
        # educamDialog = addEducamDialog.EducamDialog(builder)

        # EDUCAM360 button bind
        # addEduCamBtn = builder.get_object("add_educam_btn")
        # addEduCamBtn.connect("clicked", educamDialog.addEducam)
        

        Gtk.main()
