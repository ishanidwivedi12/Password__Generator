import random
import string
import PySimpleGUI as sg

upper = random.sample(string.ascii_uppercase, 2)
lower = random.sample(string.ascii_lowercase, 2)
digits = random.sample(string.digits, 2)
symbols = random.sample(string.punctuation, 2)
total = upper + lower + digits + symbols
total = random.sample(total, len(total))
total = ''.join(total)
print(total)

sg.set_options(font='verdana 15')

layout = [
    [sg.Text('Uppercase: '), sg.Push(), sg.Input(size=15, key='-UP-')],
    [sg.Text('Lowercase: '), sg.Push(), sg.Input(size=15, key='-LOW-')],
    [sg.Text('Digits: '), sg.Push(), sg.Input(size=15, key='-DIG-')],
    [sg.Text('Symbols: '), sg.Push(), sg.Input(size=15, key='-SYM-')],
    [sg.Button('ok'), sg.Button('cancel')],
    [sg.Text('Password'), sg.Push(), sg.Multiline(size=15, no_scrollbar=True, disabled=True, key='-PASS-')]
]

Window = sg.Window('Password Generator', layout)

while True:
    event, value = Window.read()
    if event == 'cancel' or event == sg.WIN_CLOSED:
        break
    if event == 'ok':
        try:
            u_upper = int(value['-UP-'])
            upper = random.sample(string.ascii_uppercase, u_upper)
            u_lower = int(value['-LOW-'])
            lower = random.sample(string.ascii_lowercase, u_lower)
            u_digits = int(value['-DIG-'])
            digits = random.sample(string.digits, u_digits)
            u_symbols = int(value['-SYM-'])
            symbols = random.sample(string.punctuation, u_symbols)

            total = upper + lower + digits + symbols
            total = random.sample(total, len(total))
            total = ''.join(total)
            Window['-PASS-'].update(total)
        except ValueError:
            Window['-PASS-'].update("No Valid Number")

Window.close()
