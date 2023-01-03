from __future__ import annotations
from abc import ABC, abstractmethod
from multiprocessing.process import BaseProcess

class Listener(ABC):
  __name: str
  
  def __init__(self, name: str) -> None:
    super().__init__()
    self.__name = name
    
  @property
  def name(self):
    return self.__name
  
  @abstractmethod
  def calculate(self, server: Server) -> None:
    pass
  
  @abstractmethod
  def start(self) -> BaseProcess:
    pass
  
  @abstractmethod
  def terminate(self) -> None:
    pass
    
class Server(ABC):
  
  @abstractmethod
  def add(self, client: Listener) -> None:
    pass
  
  @abstractmethod
  def notify(self) -> None:
    pass