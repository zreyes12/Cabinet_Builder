#########################################################################################
#
#   File: frame_manager.py
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
#   Class: FrameManager
#
#   Purpose: wrapper class for managing the frames.
#
#########################################################################################
class FrameManager:


    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self, container, controller):

        self.container = container
        self.controller = controller
        self.views = {}
        self.current_frame = None

        self.views = {
            "Home": HomeFrame,
            "Settings": SettingsFrame,
        }

        self.init_frames()



    #####################################################################################
    #
    #   Procedure: init_frames
    #
    #   Purpose: first call before handling any of the frames.
    #
    #####################################################################################
    def init_frames(self):

        for name, FrameClass in self.views.items():

            frame = FrameClass(parent=self.container, controller=self.controller)
            self.views[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")



    #####################################################################################
    #
    #   Procedure: set_frame
    #
    #   Purpose: Updates our current frame for our next redraw cycle.
    #
    #####################################################################################
    def set_frame(self, name):

        if name in self.views:
            self.current_frame = self.views[name]
            self.current_frame.tkraise()



    #####################################################################################
    #
    #   Procedure: get_current_frame
    #
    #   Purpose: grabs the latest frame that's been drawn.
    #
    #####################################################################################
    def get_current_frame(self):

        return self.views.get(self.current_frame)



    #####################################################################################
    #
    #   Procedure: redraw_frame
    #
    #   Purpose: redraws the latest frame. Handled from the refresh cycle.
    #            Avoid force drawing to update frames. Allow the refresh to update
    #            draws to avoid stale data.
    #
    #####################################################################################
    def redraw_frame(self):

        frame = self.get_current_frame()
        if hasattr(frame, "draw"):
            frame.draw()
