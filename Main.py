from __future__ import annotations
from abc import ABC, abstractmethod
    """
    Bot Invoker
    Quiz 1
    Diseño y arquitectura de software
    Santiago Uribe Luna
    """

class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass

class EncenderComm(Command):
	def __init__(self):
		pass
	def excecute(self):
		print("Encendido")
		
class ApagarComm(Command):
	def __init__(self):
		pass
	def excecute(self):
		print("Apagado")
		
class EncenderCommand(Command):
	def __init__(self,message):
		self.message = messsage
	def excecute(self) -> None:
		print(f"bot dice {self.message}")
		
class Bot:
	def encender(self, command):
		self.encender_comando = command
	def apagar(self, command):
		self.apagar_comando = command	
