import requests
from iwriter import IWriter


class NetworkWriter(IWriter):

    def __init__(self, url_address):
        self.url_address = url_address

    def send_data(self, data: str, machine_name: str) -> None:
        payload = {"machine": machine_name, "data": data}
        try:
            response = requests.post(self.url_address, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending data: {e}")

# TEST
# server = NetworkWriter("http://localhost:5000/save_data")
# server.send_data("Danny177", "Computer")