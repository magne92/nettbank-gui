import PySimpleGUI as sg
 
# Design pattern 2 - First window remains active
 
def login_layout():
    layout = [
            [sg.Text('LOGIN')],
            [sg.Text('Username: ')],[sg.Input(do_not_clear=True, key='-username-')],
            [sg.Text('Password: ')],[sg.Input(password_char='*',do_not_clear=True, key='-password-')],
            [sg.Text(size=(15,1), key='-wrong_PW-')],
            [sg.Button('Login'), sg.Button('Exit')]
            ]
 
    return layout
 
def bank_layout():
    layout = [[sg.Text('Welcome -name-')],
              [sg.Text('Bank balance: '),sg.Text('-amountofmoney-')],
              [sg.Button('Exit')]]
 
    return layout
 
login_win = sg.Window('Magnemaker BANK', login_layout())

username = 'magne'
password = '123'
 
login_active = True
bank_active = False

while True:
    ev1, values1 = login_win.read(timeout=100)
    #login_win['-wrong_pw-'].update(values1[0])
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break
        
    if not bank_active and ev1 == 'Login':
        if values1['-username-'] == username and values1['-password-'] == password:
            bank_active = True
        #win1.Hide()  # fjern hashtag for å skjule window 1 når window 2 skal vises
            bank_win = sg.Window('BANK', bank_layout())
            login_win.close()
        

while bank_active:
    ev2, vals2 = bank_win.read(timeout=100)
    if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
        bank_active  = False
        #win1.UnHide()   # fjern hashtag for å vise window 1 igjen
        bank_win.close()



