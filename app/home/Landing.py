import gi
import app.home.ui as ui

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk, GLib

class CreateUI:
    def __init__(self):
        print("Paining Home UI")
        self.ui = ui.UI()

class Home:
    def __init__(self):
        print("Loaded Home")
        CreateUI()