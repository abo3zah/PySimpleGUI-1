import PySimpleGUI as sg

"""
    Demo showing how to remove the titlebar and replace with your own
    Note that you cannot minimize these kinds of windows because they do not
    have an icon representing them on the taskbar
    
    Copyright 2020 PySimpleGUI.org
"""


# If not running 4.28.0.4+ that has the DarkGrey8 theme, then uncomment to get it added.
# DarkGrey8 = {'BACKGROUND': '#19232D',
#               'TEXT': '#ffffff',
#               'INPUT': '#32414B',
#               'TEXT_INPUT': '#ffffff',
#               'SCROLL': '#505F69',
#               'BUTTON': ('#ffffff', '#32414B'),
#               'PROGRESS': ('#505F69', '#32414B'),
#               'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
#               }
#
# sg.theme_add_new('DarkGrey8', DarkGrey8)

def title_bar(title):
    bg = sg.theme_input_background_color()

    return [sg.Col([[sg.T(title, background_color=bg )]], pad=(0, 0), background_color=bg),
     sg.Col([[sg.Text('❎', background_color=bg, enable_events=True, key='Exit')]], element_justification='r', k='-C-', pad=(0, 0), background_color=bg)]


def main():
    sg.theme('DarkGrey8') # Requires 4.28.0.4 or the code at the tiop
    layout = [
                title_bar('Window Title'),
                [sg.T('This is normal window text.   The above is the fake "titlebar"')],
                [sg.T('Input something:')],
                [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Go')]  ]

    window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True, keep_on_top=True, margins=(0,0), finalize=True)

    window['-C-'].expand(True, False, False)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            window['-OUT-'].update(values['-IN-'])
    window.close()

if __name__ == '__main__':
    main()