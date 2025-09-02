import datetime


class IWriter:
	def __init__(self, file_name: str):
		self.file_name = file_name

	def send_data(self, data: str, machine_name: str) -> None:
		with open(self.file_name, 'a') as file:
			file.write(f'****{self.time_taker()}****\n')
			file.write(f'****{machine_name}****\n\n')
			file.write(f'{data}\n\n\n')

	@staticmethod
	def time_taker():
		now = datetime.datetime.now()
		return now.strftime("%H:%M:%S--%d/%m/%Y")
