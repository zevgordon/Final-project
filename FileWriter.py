import datetime
from iwriter import IWriter

class FileWriter(IWriter):
    def __init__(self, path="log.txt", encoding="utf-8"):
        self.path = path
        self.encoding = encoding

    def send_data(self, payload: str, machine_name: str) -> None:
        if len(payload)>0:
            with open(self.path, "a", encoding=self.encoding, newline="") as file:
                file.write(f"****{machine_name}****\n\n")
                file.write(payload)
                file.write("\n\n")

    @staticmethod
    def time_taker():
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S--%d/%m/%Y")

