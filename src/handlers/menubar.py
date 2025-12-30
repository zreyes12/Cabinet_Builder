#########################################################################################
#
#   File: menubar.py
#
#   Purpose: handles commands for the menu bar.
#
#
#########################################################################################

import configs.constants as C
import utilities.logger
import ui.menu_bar
import tkinter as tk
from tkinter import messagebox
from ui.alert_manager import AlertManager
from utilities.app_state import AppState



#########################################################################################
#
#   Class: HandleMenuBar
#
#   Purpose: wrapper class for menu bar functionality.
#
#########################################################################################
class HandleMenuBar:


    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self, root, ViewManager, app_state):

        self.root = root
        self.app_state = app_state
        self.view_manager = ViewManager


    #####################################################################################
    #
    #   Procedure: view_home
    #
    #   Purpose: sets our current view to home.
    #
    #####################################################################################
    def view_home(self):

        self.view_manager.set_view("Home")




    #####################################################################################
    #
    #   Procedure: view_settings
    #
    #   Purpose: sets our current view to settings.
    #
    #####################################################################################
    def view_settings(self):

        self.view_manager.set_view("Settings")



    #####################################################################################
    #
    #   Procedure: select_all
    #
    #   Purpose: 
    #
    #####################################################################################
    def select_all(self):

        if self.app_state.select_all_checkbox.get():
            self.app_state.ccd_graph_checkbox.set(True)
            self.app_state.gc_graph_checkbox.set(True)
            self.app_state.tcd_graph_checkbox.set(True)
        else:
            self.app_state.ccd_graph_checkbox.set(False)
            self.app_state.gc_graph_checkbox.set(False)
            self.app_state.tcd_graph_checkbox.set(False)



    #####################################################################################
    #
    #   Procedure: use_sensor_data
    #
    #   Purpose: handles setting flags for running sensors vs simulated or imported data.
    #
    #####################################################################################
    def use_sensor_data(self):

        self.app_state.sensor_data_checkbox.set(True)



    #####################################################################################
    #
    #   Procedure: active_sensor_plotting
    #
    #   Purpose: logs which sensors we are currently plotting.
    #
    #####################################################################################
    def active_sensor_plotting(self):

        print("Active sensors now plotting:")



    #####################################################################################
    #
    #   Procedure: debug_toggle
    #
    #   Purpose: Handles the associated simulation flags for simulating the hardware.
    #
    #####################################################################################
    def debug_toggle(self):

        self.app_state.debug_mode.set(not self.app_state.debug_mode.get())
        print(f"debug_mode = {self.app_state.debug_mode.get()}")



    #####################################################################################
    #
    #   Procedure: import_file
    #
    #   Purpose: Imports recorded data into the graph to be used.
    #
    #####################################################################################
    def import_file(self):

        current_read_line = None
        while not current_read_line:
            current_read_line = "read_gas_sensor_log_file()"
        self.app_state.sensor_data_checkbox.set(False)



    #####################################################################################
    #
    #   Procedure: save_sensor_data
    #
    #   Purpose: Records the data associated with the sensors to either be used at a 
    #            later time or viewed again within the software.
    #
    #####################################################################################
    def save_sensor_data(self):

        print("save off existing data")
        #write_gas_sensor_log_file("DateHere_")
        #write_gas_sensor_log_file("log")



    #####################################################################################
    #
    #   Procedure: new_data
    #
    #   Purpose: 
    #
    #####################################################################################
    def new_data(self):

        result = AlertManager.ask_yes_no("New Data", 
                    "This will clear out any data associated with the sensors that\n"
                    "have been logged since startup of the software or last clear.\n"
                    "\n"
                    "Are you sure you want to continue?")

        if result:
            print("Clearing sensor data...")



    #####################################################################################
    #
    #   Procedure: quit_app
    #
    #   Purpose: 
    #
    #####################################################################################
    def quit_app(self):

        global running
        running = False
        self.root.destroy()

