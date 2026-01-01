#########################################################################################
#
#   File: view_manager.py
#
#   Purpose: manages available frames to draw/redraw
#
#
#########################################################################################

import configs.constants as C
import tkinter as tk
from ui.menu_bar import MenuBarConfig
from ui.views.home_view import HomeFrame
from ui.views.settings_view import SettingsFrame



#########################################################################################
#
#   Class: ViewManager
#
#   Purpose: wrapper class for managing the views.
#
#########################################################################################
class ViewManager:


    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self, parent, controller):

        self.parent = parent
        self.controller = controller
        self.views = {}
        self.current_view = None

        self.views = {
            "Home": HomeFrame,
            "Settings": SettingsFrame,
        }

        if parent.pack_slaves():
            raise RuntimeError("ViewManager parent has packed widgets.")
        self.init_views()



    #####################################################################################
    #
    #   Procedure: init_views
    #
    #   Purpose: first call before handling any of the views.
    #
    #####################################################################################
    def init_views(self):

        for name, FrameClass in self.views.items():

            view = FrameClass(self.parent, controller=self.controller)
            self.views[name] = view
            view.grid(row=0, column=0, sticky="nsew")



    #####################################################################################
    #
    #   Procedure: set_view
    #
    #   Purpose: Updates our current view for our next redraw cycle.
    #
    #####################################################################################
    def set_view(self, name):

        if name in self.views:
            self.current_view = self.views[name]
            self.current_view.tkraise()



    #####################################################################################
    #
    #   Procedure: get_current_view
    #
    #   Purpose: grabs the latest view that's been drawn.
    #
    #####################################################################################
    def get_current_view(self):

        return self.views.get(self.current_view)



    #####################################################################################
    #
    #   Procedure: redraw_view
    #
    #   Purpose: redraws the latest view. Handled from the refresh cycle.
    #            Avoid force drawing to update frames. Allow the refresh to update
    #            draws to avoid stale data.
    #
    #####################################################################################
    def redraw_view(self):

        frame = self.get_current_view()
        if hasattr(frame, "draw"):
            frame.draw()
