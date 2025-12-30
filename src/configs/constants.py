#########################################################################################
#
#   File: constants.py
#
#   Purpose: Global constants for the application.
#
#########################################################################################


#App Information
COMPANY                      = "Zack"
CONTACT                      = "580-339-2264"
TITLE                        = "Cabinet Builder"
VERSION                      = "1.0.0"

#TK window properties
DEFAULT_WINDOW_SIZE          = "1100x700"
DEFAULT_CURSOR               = "arrow"

# Colors
DEFAULT_BG_COLOR             = "lightgrey"
DEFAULT_FG_COLOR             = "black"
DEFAULT_BORDER_COLOR         = "black"


#Default Data
DEFAULT_SENSOR_DATA          = "No Data"
DEFAULT_STATUS_TEXT          = "Initializing..."


# Refresh timing (in milliseconds)
ONE_HERTZ                    = 1000
TWO_HERTZ                    = 500
FOUR_HERTZ                   = 250
EIGHT_HERTZ                  = 125

# Fonts and styles
DEFAULT_FONT                 = ('Arial', 14)
DEFAULT_BOLD                 = ('Arial', 14, "bold")
HEADER_BOLD                  = ('Arial', 20, "bold")
DEFAULT_PAD                  = 5
PARENT_BD_THICKNESS          = 2
CHILD_BD_THICKNESS           = 1

#########################################################################################
#Frame Styles
#########################################################################################
PARENT_FRAME_STYLE = {
    "bg"                  : DEFAULT_BG_COLOR,
}


PARENT_BORDER_FRAME_STYLE = {
    "bg"                  : DEFAULT_BORDER_COLOR,
    "bd"                  : PARENT_BD_THICKNESS,
    "relief"              : "solid"

}


CHILD_FRAME_STYLE = {
    "bg"                  : DEFAULT_BG_COLOR,
    "padx"                : DEFAULT_PAD,
    "pady"                : DEFAULT_PAD
}


CHILD_BORDER_FRAME_STYLE = {
    "bg"                  : DEFAULT_BORDER_COLOR,
    "bd"                  : CHILD_BD_THICKNESS,
    "relief"              : "solid"

}


#########################################################################################
#Widget Styles
#########################################################################################
HEADER_LABEL_STYLE = {
    "font"                : HEADER_BOLD,
    "fg"                  : "black",
    "bg"                  : "lightgrey",
    "padx"                : DEFAULT_PAD,
    "pady"                : DEFAULT_PAD,
}


DEFAULT_LABEL_STYLE = {
    "font"                : DEFAULT_FONT,
    "fg"                  : "black",
    "bg"                  : "lightgrey",
    "padx"                : DEFAULT_PAD,
    "pady"                : DEFAULT_PAD,
}


DEFAULT_BUTTON_STYLE = {
    "font"                : DEFAULT_BOLD,
    "fg"                  : "black",
    "bg"                  : "lightgrey",
    "padx"                : DEFAULT_PAD,
    "pady"                : DEFAULT_PAD,
    "cursor"              : "hand2",
    "bd"                  : 5,
    "highlightthickness"  : 2,
    "activebackground"    : "blue",
    "activeforeground"    : "white"
}




#Common Values
UPPER_FROM_FLOOR             = 54
UPPER_FROM_COUNTERTOP        = 18
UPPER_FROM_COOKTOP           = 30

#Wood Values
PLYWOOD_THICKNESS            = .75
#actually 11/16 and probably need to add list here to select thickness size.
HARDWOOD_THICKNESS           = .75

#Common Cabinet Sizes Lowers
STANDARD_BASE_HEIGHT         = 34.5
STANDARD_BASE_DEPTH          = 24
STANDARD_BASE_BATHROOM_DEPTH = 21
TALL_BASE_HEIGHT             = 36

#Fractions
FRACTIONS = {
    "a" : "1/6",
    "b" : "1/8",
    "c" : "3/16",
    "d" : "1/4",
    "e" : "5/16",
    "f" : "3/8",
    "g" : "7/16",
    "h" : "1/2",
    "i" : "9/16",
    "j" : "5/8",
    "k" : "3/4",
    "l" : "11/16",
    "m" : "5/8",
    "n" : "3/4",
    "o" : "13/16",
    "p" : "7/8",
    "q" : "15/16"
}

#Common Cabinet Widths
COMMON_WIDTHS = {
    "a" : 9,
    "b" : 12,
    "c" : 15,
    "d" : 18,
    "e" : 21,
    "f" : 24,
    "g" : 27,
    "h" : 30,
    "i" : 33,
    "j" : 36
}

#Common Cabinet Sizes Uppers
SLIM_UPPER_DEPTH             = 12
OVER_FRIDGE_UPPER_DEPTH      = 24

SLIM_UPPER_HEIGHT = {
    "a" : 12,
    "b" : 13,
    "c" : 14,
    "d" : 15,
    "e" : 16,
    "f" : 17,
    "g" : 18,
}

PANTRY_UPPER_HEIGHT = {
    "a" : 30,
    "b" : 31,
    "c" : 32,
    "d" : 33,
    "e" : 34,
    "f" : 35,
    "g" : 36,
    "h" : 37,
    "i" : 38,
    "j" : 39,
    "k" : 40,
    "l" : 41,
    "m" : 42
}

OVER_FRIDGE_UPPER_HEIGHT = {
    "a" : 12,
    "b" : 13,
    "c" : 14,
    "d" : 15,
    "e" : 16,
    "f" : 17,
    "g" : 18,
    "h" : 19,
    "i" : 20,
    "j" : 21,
    "k" : 22,
    "l" : 23,
    "m" : 24
}


PANTRY_UPPER_DEPTH = {
    "a" : 12,
    "b" : 13,
    "c" : 14,
    "d" : 15,
    "e" : 16,
    "f" : 17,
    "g" : 18,
    "h" : 19,
    "i" : 20,
    "j" : 21,
    "k" : 22,
    "l" : 23,
    "m" : 24
}


#Cabinet components
FACE_THICKNESS               = HARDWOOD_THICKNESS
HEADER                       = 4
STYLE                        = 2
TOE_KICK_HEIGHT              = 4.5
TOE_KICK_DEPTH               = 3

