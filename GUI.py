from main import *
import json
import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')
ttk_style = 'clam'




# Define the window's contents
layout = [[sg.Text("Enter player NameTag")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(20,1), key='-OUTPUT-')],
          [sg.Button('Ok', use_ttk_buttons=True) , sg.Button('Quit', use_ttk_buttons=True)]]



# Create the window
window = sg.Window('Window Title', layout, ttk_theme=ttk_style)




# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    try:
        WriteIntoFile(values['-INPUT-'])

        with open('data.json') as f:
            d = json.load(f)

        bw = d.get('player', {}).get('stats', {}).get('Bedwars', {})

        sg.popup_scrolled(json.dumps(bw, indent=2), title='Bedwars stats', size=(60, 20))
        
    except Exception as e:
        sg.popup_error(f'Error: {e}')

window.close()












# Finish up by removing from the screen
window.close()


