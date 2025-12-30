#########################################################################################
#
#   File: settings_view.py
#
#   Purpose: Configures and handles the avialable items for the settings view.
#
#
#########################################################################################

import configs.constants as C
import tkinter as tk



#########################################################################################
#
#   Class: SettingsFrame
#
#   Purpose: wrapper class for handling the Settings view.
#
#########################################################################################
class SettingsFrame(tk.Frame):


    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self, parent, controller):

        super().__init__(parent)

        self.controller = controller
        self.dynamic_widgets = []
        self.build()



    #####################################################################################
    #
    #   Procedure: build
    #
    #   Purpose: configures the layout of the frame.
    #
    #####################################################################################
    def build(self):


        header_label = tk.Label(self, 
                                text="Settings", 
                                **C.DEFAULT_LABEL_STYLE)
        
        header_label.grid(row=0,
                          column=0,
                          padx=C.DEFAULT_PAD,
                          pady=C.DEFAULT_PAD)

        self.dynamic_area = tk.Frame(self)
        
        self.dynamic_area.grid(row=0,
                               column=0,
                               padx=C.DEFAULT_PAD,
                               pady=C.DEFAULT_PAD)

        self.draw()



    #####################################################################################
    #
    #   Procedure: clear
    #
    #   Purpose: clears out the frames items. Always called before drawing.
    #
    #####################################################################################
    def clear(self):
        for widget in self.dynamic_widgets:
            widget.destroy()
        self.dynamic_widgets.clear()



    #####################################################################################
    #
    #   Procedure: draw
    #
    #   Purpose: 
    #
    #####################################################################################
    def draw(self):

        self.clear()

        button = tk.Button(self.dynamic_area,
                           text="Settings Refreshed")
        button.grid(row=0,
                    column=0,
                    padx=C.DEFAULT_PAD,
                    pady=C.DEFAULT_PAD)

        self.dynamic_widgets.append(button)