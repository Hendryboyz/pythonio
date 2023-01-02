from pythonio.observers.interface import Listener, Server
from multiprocessing.process import BaseProcess
from multiprocessing.sharedctypes import SynchronizedArray
from multiprocessing import Process, Array


def run_client_3(nums: SynchronizedArray):
  print('Client3 is ready')

class SharedMemoryListener(Listener):
  def __init__(self, name: str) -> None:
    super().__init__(name)
    
  def start(self) -> BaseProcess:
    super().start()
    nums = Array('i', ())
    p = Process(target=run_client_3, args=(nums,))
    p.start()
    return p
    
  def calculate(self, server: Server) -> None:
    super().calculate(server)