from abc import ABC, abstractmethod
import datetime


class IWriter(ABC):
	#@abstractmethod
	def send_data(self, data: str) -> None:
		#machine_name: str
		with open('log.txt', 'a') as file:
			file.write(f'****{self.time_taker()}****\n')
		#	file.write(f'****{machine_name}****\n')
			file.write(f'{data}\n')

	@abstractmethod
	def time_taker(self):
		now = datetime.datetime.now()
		return now.strftime("%H:%M:%S--%d/%m/%Y")
