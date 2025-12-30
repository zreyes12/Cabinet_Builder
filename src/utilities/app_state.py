#########################################################################################
#
#   File: app_state.py
#
#   Purpose: Holds application level variables.
#
#
#########################################################################################

import tkinter as tk



#########################################################################################
#
#   Class: AppState
#
#   Purpose: wrapper class for managing state variables,
#            gets called on startup.
#
#########################################################################################
class AppState:


    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self):

        self.debug_mode = tk.BooleanVar(value=True)
        self.current_depth = tk.DoubleVar(value=0.0)
        self.safe_threshold = tk.DoubleVar(value=1000.0)
        self.test_values = tk.DoubleVar(value=0.0)


        self.auto_gain_checkbox = tk.BooleanVar(value=True)
        self.debug_mode_checkbox = tk.BooleanVar(value=True)
        self.select_all_checkbox = tk.BooleanVar(value=True)
        self.ccd_graph_checkbox = tk.BooleanVar(value=True)
        self.gc_graph_checkbox = tk.BooleanVar(value=True)
        self.tcd_graph_checkbox = tk.BooleanVar(value=True)
        self.threshold_line_checkbox = tk.BooleanVar(value=True)
        self.sensor_data_checkbox = tk.BooleanVar(value=True)

        self.total_frames_drawn = tk.IntVar(value=0)