#########################################################################################
#
#   File: refresh_controller.py
#
#   Purpose: manages our refresh cycles for spliting out the logic
#            between hardware redraw cycles.
#
#########################################################################################

import configs.constants as C
from ui.view_manager import ViewManager



#########################################################################################
#
#   Class: RefreshController
#
#   Purpose: wrapper class for managing refresh cycles.
#
#########################################################################################
class RefreshController:


    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self, root, manager):

        self.root = root
        self.manager = manager



    #####################################################################################
    #
    #   Procedure: start_refresh_cycles
    #
    #   Purpose: Starts our loop for calling our available refresh cycles.
    #
    #####################################################################################
    def start_refresh_cycles(self):

        self.refresh_2hz()
        self.refresh_4hz()



    #####################################################################################
    #
    #   Procedure: refresh_2hz
    #
    #   Purpose: manages everything refreshed at 2Hz
    #
    #####################################################################################
    def refresh_2hz(self):

        print("[2Hz] Refreshing")
        self.manager.redraw_view()
        self.root.after(C.TWO_HERTZ, self.refresh_2hz)



    #####################################################################################
    #
    #   Procedure: refresh_4hz
    #
    #   Purpose: manages everything refreshed at 4Hz
    #
    #####################################################################################
    def refresh_4hz(self):

        print("[4Hz] Refreshing")
        self.root.after(C.FOUR_HERTZ, self.refresh_4hz)