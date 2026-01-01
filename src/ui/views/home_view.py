#########################################################################################
#
#   File: home_view.py
#
#   Purpose: Configures and handles the avialable items for the home view
#
#
#########################################################################################

import configs.constants as C
import tkinter as tk
from tkinter import ttk
from ui.views.base_view import BaseView
from ui.alert_manager import AlertManager

#########################################################################################
#
#   Class: HomeFrame
#
#   Purpose: wrapper class for handling the home view.
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
        self.grid_rowconfigure(0,weight=1)

        # Define the different types of cabinets able to be used.
        self.cabinet_types = [
            ("Upper"       , "upper"       ),
            ("Lower"       , "lower"       ),
            ("Over Range"  , "over_range"  ),
            ("Over Fridge" , "over_fridge" ),
            ("Custom"      , "custom"      ),
        ]

        # Define label configurations
        self.label_rows = [
            # row, name_prefix, label text, data input, fraction, units
            (2, "height" , "Height:" , C.SLIM_UPPER_HEIGHT , C.FRACTIONS , "Inches" ),
            (3, "width"  , "Width:"  , C.COMMON_WIDTHS     , C.FRACTIONS , "Inches" ),
            (4, "depth"  , "Depth:"  , C.SLIM_UPPER_DEPTH  , C.FRACTIONS , "Inches" ),
        ]

        self.build()



    #####################################################################################
    #
    #   Procedure: build
    #
    #   Purpose: configures the  layout of the frame.
    #
    #####################################################################################
    def build(self):

        self.home_border_frame = tk.Frame(
            self,
            **C.PARENT_BORDER_FRAME_STYLE
        )

        self.home_border_frame.pack(fill="both", expand=True)
        self.home_border_frame.grid_rowconfigure(0, weight=1)
        self.home_border_frame.grid_columnconfigure(0, weight=1)

        self.home_child_frame = tk.Frame(
            self.home_border_frame,
            **C.CHILD_FRAME_STYLE
        )

        self.home_child_frame.pack(fill="both", expand=True)
        self.home_child_frame.grid_rowconfigure(0, weight=1)
        self.home_child_frame.grid_columnconfigure(0, weight=1)






        self.cabinet_specs_parent_frame = tk.Frame(
            self.home_child_frame,
            **C.PARENT_FRAME_STYLE
        )

        self.cabinet_specs_parent_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


        self.cabinet_specs_border_frame = tk.Frame(
            self.cabinet_specs_parent_frame,
            **C.PARENT_BORDER_FRAME_STYLE
        )

        self.cabinet_specs_border_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.cabinet_specs_frame = tk.Frame(
            self.cabinet_specs_border_frame,
            **C.CHILD_FRAME_STYLE
        )

        self.cabinet_specs_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )




        self.radio_border_frame = tk.Frame(
            self.cabinet_specs_frame,
            **C.CHILD_BORDER_FRAME_STYLE
        )

        self.radio_border_frame.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="n"
        )



        self.radio_frame = tk.Frame(
            self.radio_border_frame,
            **C.CHILD_FRAME_STYLE
        )


        self.radio_frame.grid(
            row = 1,
            column=0,
            rowspan=2,
            columnspan=4,
            sticky="n",
        )


        self.graph_area = tk.Frame(
            self.home_child_frame,
            bg = "green"
        )

        self.graph_area.grid(
            row=0,
            column=1,
            sticky="n"
        )

        self.cabinet_specs_parent_frame.grid_columnconfigure(0, weight=0)
        self.cabinet_specs_parent_frame.grid_rowconfigure(0, weight=0)

        self.cabinet_specs_border_frame.grid_columnconfigure(0, weight=0)
        self.cabinet_specs_border_frame.grid_rowconfigure(0, weight=0)

        self.cabinet_specs_frame.grid_rowconfigure(5, weight=1)

        self.draw()



    #####################################################################################
    #
    #   Procedure: clear
    #
    #   Purpose: clears out the frames items.
    #
    #####################################################################################
    def clear(self):

        for widget in self.dynamic_widgets:
            widget.destroy()
        self.dynamic_widgets.clear()
        self.selected_vars.clear()


    #####################################################################################
    #
    #   Procedure: draw
    #
    #   Purpose: 
    #
    #####################################################################################
    def draw(self):


        self.clear()


        def show_value():

            print("Cabinet type:", self.cabinet_type_text.get())

            print("check for button press")
            for key, var in self.selected_vars.items():
                print(f" {key}: {var.get()}")



        header_label = tk.Label(
            self.cabinet_specs_frame, 
            text="Single Cabinet Mode", 
            **C.HEADER_LABEL_STYLE
        )

        header_label.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="n"
        )




        label = tk.Label(
            self.radio_frame, 
            text="Cabinet Type", 
            **C.DEFAULT_LABEL_STYLE
            )

        label.pack(side="left")
        self.dynamic_widgets.append(label)

        self.cabinet_type_text = tk.StringVar(value="upper")

        for text, value in self.cabinet_types:

            rb = tk.Radiobutton(
                self.radio_frame,
                text=text,
                bg=C.DEFAULT_BG_COLOR,
                variable=self.cabinet_type_text,
                value=value,
                anchor="n"
            )

            rb.pack(side="left", padx=8)
            self.dynamic_widgets.append(rb)


        # Loop to create and place widgets
        for row, key, label_text, data_input, fraction, units in self.label_rows:
            # Left label (descriptor)
            label = tk.Label(self.cabinet_specs_frame, 
                             text=label_text, 
                             **C.DEFAULT_LABEL_STYLE)

            label.grid(row=row, column=0, sticky="ne")
            self.labels[f"{key}_label"] = label
            self.dynamic_widgets.append(label)

            # Center value (data)
            if data_input:
                if isinstance(data_input, dict):

                    default_value = next(iter(data_input.values()))
                    default_value_text = tk.StringVar(value=default_value)
                    self.selected_vars[key] = default_value_text

                    combo1 = ttk.Combobox(
                        self.cabinet_specs_frame,
                        textvariable=default_value_text,
                        values=list(data_input.values()),
                        state="readonly",
                        width=30,
                        height=5
                    )

                    combo1.grid(row=row, column=1)
                    self.dynamic_widgets.append(combo1)

                else:

                    test_label = tk.Label(
                        self.cabinet_specs_frame,
                        text=data_input,
                        **C.DEFAULT_LABEL_STYLE
                    )

                    test_label.grid(row=row, column=1, sticky="n")
                    self.dynamic_widgets.append(test_label)


            # Center value (data)
            if fraction:

                default_fraction = next(iter(fraction.values()))
                default_fraction_text = tk.StringVar(value=default_fraction)
                self.selected_vars[key] = default_value_text

                combo2 = ttk.Combobox(
                    self.cabinet_specs_frame,
                    textvariable=default_fraction_text,
                    values=list(fraction.values()),
                    state="readonly",
                    width=10,
                    height=5
                )

                combo2.grid(row=row, column=2)
                self.dynamic_widgets.append(combo2)

            # Right label (units)
            if units:

                unit_label = tk.Label(
                    self.cabinet_specs_frame, 
                    text=units, 
                    **C.DEFAULT_LABEL_STYLE
                )

                unit_label.grid(row=row, column=3, sticky="nw")
                self.labels[f"{key}_unit"] = unit_label
                self.dynamic_widgets.append(unit_label)



        lumber_button = tk.Button(
            self.cabinet_specs_frame,
            text="Lumber",
            command=show_value,
            **C.DEFAULT_BUTTON_STYLE
        )

        lumber_button.grid(
            row=5,
            column=0,
            sticky="nw"
        )

        self.dynamic_widgets.append(lumber_button)


        cut_list_button = tk.Button(
            self.cabinet_specs_frame,
            text="Cut List",
            command=show_value,
            **C.DEFAULT_BUTTON_STYLE
        )

        cut_list_button.grid(
            row=5,
            column=3,
            sticky="ne"
        )

        self.dynamic_widgets.append(cut_list_button)