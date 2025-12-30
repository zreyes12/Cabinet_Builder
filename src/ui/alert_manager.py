#########################################################################################
#
#   File: alert_manager.py
#
#   Purpose: Holds the procedural calls for the different types of alerts.
#
#
#########################################################################################

import configs.constants as C
from tkinter import messagebox



#########################################################################################
#
#   Class: AlertManager
#
#   Purpose: wrapper class for the available alerts. Each procedure is independent.
#
#########################################################################################
class AlertManager:


    #####################################################################################
    #
    #   Procedure: show_about
    #   Purpose: Message box for the software version
    #
    #####################################################################################
    @staticmethod
    def show_about():

        messagebox.showinfo("About", 
                            f"Version: {C.VERSION}")



    #####################################################################################
    #
    #   Procedure: show_contact
    #   Purpose: Message box for the company contact info
    #
    #####################################################################################
    @staticmethod
    def show_contact():

        messagebox.showinfo(
            "Contact",
            f"Company: {C.COMPANY}\n"
            f"Contact: {C.CONTACT}")



    #####################################################################################
    #
    #   Procedure: show_error
    #   Purpose: Message box for returning errors to the user.
    #
    #####################################################################################
    @staticmethod
    def show_error(title, message):
        messagebox.showerror(title, message)



    #####################################################################################
    #
    #   Procedure: show_warning
    #   Purpose: Message box for returning a warning to the user.
    #
    #####################################################################################
    @staticmethod
    def show_warning(title, message):

        messagebox.showwarning(title, message)



    #####################################################################################
    #
    #   Procedure: show_info
    #   Purpose: Message box for displaying user required awareness information.
    #
    #####################################################################################
    @staticmethod
    def show_info(title, message):

        messagebox.showinfo(title, message)



    #####################################################################################
    #
    #   Procedure: ask_yes_no
    #   Purpose: Message box for verifying user wants to continue
    #
    #####################################################################################
    @staticmethod
    def ask_yes_no(title, message):
        return messagebox.askyesno(title, message)