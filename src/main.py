#########################################################################################
#
#   File: main.py
#
#   Purpose: main entry point for our tkinter app.
#
#
#########################################################################################


import tkinter as tk
from ui.menu_bar import MenuBarConfig
from ui.view_manager import ViewManager
from ui.views.home_view import HomeFrame
from controllers.refresh_controller import RefreshController
from utilities.app_state import AppState
import configs.constants as C


#########################################################################################
#
#   Class: App
#
#   Purpose: wrapper class for our root application.
#
#########################################################################################
class App(tk.Tk):

    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self):

        super().__init__()

        self.setup_root()
        self.setup_container()
        self.setup_managers()
        self.setup_menu()
        self.on_app_ready()

    #####################################################################################
    #
    #   Procedure: setup_root
    #
    #   Purpose: Configures & initalizes our required tk root window variables.
    #
    #####################################################################################
    def setup_root(self):

        self.title(C.TITLE)
        self.geometry(C.DEFAULT_WINDOW_SIZE)
        self.config(bg=C.DEFAULT_BG_COLOR)
        self.config(cursor=C.DEFAULT_CURSOR)



    #####################################################################################
    #
    #   Procedure: setup_container
    #
    #   Purpose: sets up the root tk frame that all other frames inherit from.
    #
    #####################################################################################
    def setup_container(self):

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)



    #####################################################################################
    #
    #   Procedure: setup_managers
    #
    #   Purpose: initializes our managers for our root app..
    #
    #####################################################################################
    def setup_managers(self):

        self.view_manager = ViewManager(self.container, self)
        self.view_manager.set_view("Home")
        self.app_state = AppState()


    #####################################################################################
    #
    #   Procedure: setup_menu
    #
    #   Purpose: initializes our root menu for our app.
    #
    #####################################################################################
    def setup_menu(self):

        self.config(menu=MenuBarConfig(self, self.view_manager, self.app_state))



    #####################################################################################
    #
    #   Procedure: on_app_ready
    #
    #   Purpose: starts our post initialization phase
    #
    #####################################################################################
    def on_app_ready(self):


        self.refresh_controller = RefreshController(self, self.view_manager)
        self.refresh_controller.start_refresh_cycles()



#########################################################################################
#   Entry Point
#########################################################################################
if __name__ == "__main__":
    app = App()
    app.mainloop()