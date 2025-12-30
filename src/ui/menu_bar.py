#########################################################################################
#
#   File: menu_bar.py
#
#   Purpose: Configures the menu bar for the root tk aplication.
#
#
#########################################################################################

import configs.constants as C
import tkinter as tk
from handlers.menubar import HandleMenuBar
from ui.alert_manager import AlertManager
from utilities.app_state import AppState



#########################################################################################
#
#   Class: HandleMenuBar
#
#   Purpose: wrapper class for menu bar functionality.
#
#########################################################################################
class MenuBarConfig(tk.Menu):


    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self, root, frame_manager, app_state):

        super().__init__(root)
        self.root = root
        self.frame_manager = frame_manager
        self.app_state = app_state

        self.menu_handlers = HandleMenuBar(root, frame_manager, app_state)
        self.build()



    #####################################################################################
    #
    #   Procedure: build
    #
    #   Purpose: Configures the available options for the menu bar.
    #
    #####################################################################################
    def build(self):

        #Root->menu_bar->File
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="New",
                              command=self.menu_handlers.new_data)
        
        file_menu.add_command(label="Import",
                              command=self.menu_handlers.import_file)
        
        file_menu.add_command(label="Save",
                              command=self.menu_handlers.save_sensor_data)
        
        file_menu.add_separator()
        file_menu.add_command(label="Exit",
                              command=self.menu_handlers.quit_app)

        self.add_cascade(label="File", menu=file_menu)


        #Root->menu_bar->View
        view_menu = tk.Menu(self, tearoff=0)
        view_menu.add_command(label="Home",
                              command=self.menu_handlers.view_home)

        view_menu.add_command(label="Settings",
                              command=self.menu_handlers.view_settings)
        self.add_cascade(label="View", menu=view_menu)


        #Root->menu_bar->Graph
        graph_menu = tk.Menu(self, tearoff=0)
        active_sensors = tk.Menu(graph_menu, tearoff=0)

        graph_menu.add_checkbutton(label="Sensor_Data",
                                   variable=self.app_state.sensor_data_checkbox,
                                   command=self.menu_handlers.use_sensor_data)


        #Root->menu_bar->Graph->Active Sensors
        active_sensors.add_checkbutton(label="Select All",
                                       variable=self.app_state.select_all_checkbox,
                                       command=self.menu_handlers.active_sensor_plotting)
        active_sensors.add_separator()
        active_sensors.add_checkbutton(label="CCD",
                                       variable=self.app_state.ccd_graph_checkbox,
                                       command=self.menu_handlers.active_sensor_plotting)

        active_sensors.add_checkbutton(label="GC",
                                       variable=self.app_state.gc_graph_checkbox,
                                       command=self.menu_handlers.active_sensor_plotting)

        active_sensors.add_checkbutton(label="TCD",
                                       variable=self.app_state.tcd_graph_checkbox,
                                       command=self.menu_handlers.active_sensor_plotting)

        graph_menu.add_cascade(label="Active Sensors", menu=active_sensors)

        graph_menu.add_separator()

        graph_menu.add_checkbutton(label="Threshold Line",
                                   variable=self.app_state.threshold_line_checkbox,
                                   command=self.menu_handlers.active_sensor_plotting)

        self.add_cascade(label="Graph", menu=graph_menu)


        #Root->menu_bar->Developer Mode
        dev_menu = tk.Menu(self, tearoff=0)

        dev_menu.add_checkbutton(label="Debug Mode",
                                 variable=self.app_state.debug_mode_checkbox,
                                 command=self.menu_handlers.debug_toggle)

        dev_menu.add_checkbutton(label="Auto Gain",
                                 variable=self.app_state.auto_gain_checkbox,
                                 command=self.menu_handlers.debug_toggle)

        self.add_cascade(label="Developer Mode", menu=dev_menu)


        #Root->menu_bar->Help
        help_menu = tk.Menu(self, tearoff=0)

        help_menu.add_command(label="About",
                              command=AlertManager.show_about)

        help_menu.add_command(label="Contact",
                              command=AlertManager.show_contact)
        
        self.add_cascade(label="Help", menu=help_menu)
