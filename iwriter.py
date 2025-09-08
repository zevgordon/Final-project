from abc import ABC, abstractmethod

class IWriter(ABC):
    
    @abstractmethod
    def send_data(self, data: str, machine_name: str,the_time :str) -> None:
        pass
