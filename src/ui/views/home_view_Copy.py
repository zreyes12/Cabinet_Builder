#########################################################################################
#
#   File: home_view.py
#
#   Purpose: Configures and handles the available items for the home view
#
#########################################################################################

import tkinter as tk
from tkinter import ttk

import configs.constants as C
from ui.views.base_view import BaseView
from ui.alert_manager import AlertManager


#########################################################################################
#
#   Class: HomeFrame
#
#########################################################################################
class HomeFrame(BaseView):

    #####################################################################################
    #   Procedure: __init__
    #####################################################################################
    def __init__(self, parent, controller):

        super().__init__(parent, controller)

        self.controller = controller
        self.dynamic_widgets = []
        self.labels = {}
        self.selected_vars = {}

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # Cabinet type radio options
        self.cabinet_types = [
            ("Upper",        "upper"),
            ("Lower",        "lower"),
            ("Over Range",   "over_range"),
            ("Over Fridge",  "over_fridge"),
            ("Custom",       "custom"),
        ]

        self.cabinet_type_text = tk.StringVar(value="upper")

        self.build()


    #####################################################################################
    #   Procedure: build
    #####################################################################################
    def build(self):

        self.home_border_frame = tk.Frame(self, **C.PARENT_BORDER_FRAME_STYLE)
        self.home_border_frame.pack(fill="both", expand=True)

        self.home_child_frame = tk.Frame(
            self.home_border_frame,
            **C.CHILD_FRAME_STYLE
        )
        self.home_child_frame.pack(fill="both", expand=True)

        self.cabinet_specs_parent_frame = tk.Frame(
            self.home_child_frame,
            **C.PARENT_FRAME_STYLE
        )
        self.cabinet_specs_parent_frame.grid(row=0, column=0, sticky="nsew")

        self.cabinet_specs_border_frame = tk.Frame(
            self.cabinet_specs_parent_frame,
            **C.PARENT_BORDER_FRAME_STYLE
        )
        self.cabinet_specs_border_frame.grid(row=0, column=0, sticky="nsew")

        self.cabinet_specs_frame = tk.Frame(
            self.cabinet_specs_border_frame,
            **C.CHILD_FRAME_STYLE
        )
        self.cabinet_specs_frame.grid(row=0, column=0, sticky="nsew")

        self.radio_border_frame = tk.Frame(
            self.cabinet_specs_frame,
            **C.CHILD_BORDER_FRAME_STYLE
        )
        self.radio_border_frame.grid(row=1, column=0, columnspan=4, sticky="n")

        self.radio_frame = tk.Frame(
            self.radio_border_frame,
            **C.CHILD_FRAME_STYLE
        )
        self.radio_frame.grid(row=0, column=0, sticky="n")

        self.graph_area = tk.Frame(self.home_child_frame, bg="green")
        self.graph_area.grid(row=0, column=1, sticky="n")

        self.draw()


    #####################################################################################
    #   Procedure: clear
    #####################################################################################
    def clear(self):

        for widget in self.dynamic_widgets:
            widget.destroy()

        self.dynamic_widgets.clear()
        self.selected_vars.clear()


    #####################################################################################
    #   Procedure: get_label_rows
    #####################################################################################
    def get_label_rows(self):

        cabinet = self.cabinet_type_text.get()
        profile = C.CABINET_PROFILES[cabinet]

        return [
            (2, "height", "Height:", profile["height"], C.FRACTIONS, "Inches"),
            (3, "width",  "Width:",  profile["width"],  C.FRACTIONS, "Inches"),
            (4, "depth",  "Depth:",  profile["depth"],  C.FRACTIONS, "Inches"),
        ]


    #####################################################################################
    #   Procedure: draw
    #####################################################################################
    def draw(self):

        self.clear()

        def show_value():
            print("Cabinet type:", self.cabinet_type_text.get())
            for key, value in self.selected_vars.items():
                print(key, value)

        # Header
        header_label = tk.Label(
            self.cabinet_specs_frame,
            text="Single Cabinet Mode",
            **C.HEADER_LABEL_STYLE
        )
        header_label.grid(row=0, column=0, columnspan=4, sticky="n")
        self.dynamic_widgets.append(header_label)

        # Radio buttons
        label = tk.Label(
            self.radio_frame,
            text="Cabinet Type",
            **C.DEFAULT_LABEL_STYLE
        )
        label.pack(side="left")
        self.dynamic_widgets.append(label)

        for text, value in self.cabinet_types:
            rb = tk.Radiobutton(
                self.radio_frame,
                text=text,
                bg=C.DEFAULT_BG_COLOR,
                variable=self.cabinet_type_text,
                value=value,
                command=self.draw
            )
            rb.pack(side="left", padx=8)
            self.dynamic_widgets.append(rb)

        # Dynamic input rows
        for row, key, label_text, data_input, fraction, units in self.get_label_rows():

            label = tk.Label(
                self.cabinet_specs_frame,
                text=label_text,
                **C.DEFAULT_LABEL_STYLE
            )
            label.grid(row=row, column=0, sticky="ne")
            self.dynamic_widgets.append(label)

            # Whole value combobox
            whole_var = tk.StringVar(
                value=next(iter(data_input.values())) if data_input else ""
            )

            self.selected_vars[key] = {
                "whole": whole_var
            }

            combo_whole = ttk.Combobox(
                self.cabinet_specs_frame,
                textvariable=whole_var,
                values=list(data_input.values()),
                state="readonly",
                width=30
            )
            combo_whole.grid(row=row, column=1)
            self.dynamic_widgets.append(combo_whole)

            # Fraction combobox
            frac_var = tk.StringVar(value=next(iter(fraction.values())))
            self.selected_vars[key]["fraction"] = frac_var

            combo_frac = ttk.Combobox(
                self.cabinet_specs_frame,
                textvariable=frac_var,
                values=list(fraction.values()),
                state="readonly",
                width=10
            )
            combo_frac.grid(row=row, column=2)
            self.dynamic_widgets.append(combo_frac)

            unit_label = tk.Label(
                self.cabinet_specs_frame,
                text=units,
                **C.DEFAULT_LABEL_STYLE
            )
            unit_label.grid(row=row, column=3, sticky="nw")
            self.dynamic_widgets.append(unit_label)

        # Buttons
        lumber_button = tk.Button(
            self.cabinet_specs_frame,
            text="Lumber",
            command=show_value,
            **C.DEFAULT_BUTTON_STYLE
        )
        lumber_button.grid(row=5, column=0, sticky="nw")
        self.dynamic_widgets.append(lumber_button)

        cut_list_button = tk.Button(
            self.cabinet_specs_frame,
            text="Cut List",
            command=show_value,
            **C.DEFAULT_BUTTON_STYLE
        )
        cut_list_button.grid(row=5, column=3, sticky="ne")
        self.dynamic_widgets.append(cut_list_button)
