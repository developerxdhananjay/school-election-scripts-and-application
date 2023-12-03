#According to Alan Turing Theorm, The Events Can Be Classified By Using Python.
#Code By Dhananjay JS. Copyright 2023
from pynput.keyboard import Key, Listener
import os
import notify2


def on_press(key):
    os.system("beep -f 3000 -l 1500")
    notify2.init('Sammaty')
    n = notify2.Notification('Start Election 2023-24', 'Next Voter')
    n.show()

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
