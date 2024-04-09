import pynput
from time import sleep
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput import keyboard

mouse = pynput.mouse.Controller()
time_interval = float(input('How much delay between clicks? (In seconds)'))
sleep(1)
print(f'You have set the autoclicker to {time_interval} seconds. To activate and deactivate autoclicker hit Control H!')
clicker_live = False

def on_activate():
    global clicker_live
    if clicker_live == True:
        clicker_live = False
        print('autoclicker turned off!')
        sleep(0.8)
    else:
        print('autoclicker turned on!')
        clicker_live = True
        sleep(0.8)

listener = keyboard.GlobalHotKeys({
'<ctrl>+h': on_activate})

listener.start()

while True:
    if clicker_live == True:
        mouse.click(Button.left)
        sleep(time_interval)