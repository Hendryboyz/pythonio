from pythonio.observers.interface import Listener, Server
from pythonio.utils.calculate import mode
from multiprocessing.process import BaseProcess
from multiprocessing.managers import ListProxy
from multiprocessing import Process, Manager
from time import sleep

def mode_client(nums: ListProxy):
  print('Client3 is ready')
  while True:
    sleep(1)
    if len(nums) > 0:
      numsMode = ', '.join(map(str, mode(nums)))
      print(f'Mode is	{numsMode}')
      nums[:] = []
    else:
      continue

class SharedMemoryListener(Listener):
  __shared_nums: ListProxy = None
  __process: BaseProcess = None
  
  def __init__(self, name: str) -> None:
    super().__init__(name)
    
  def start(self) -> BaseProcess:
    super().start()
    manager = Manager()
    self.__shared_nums = manager.list([])
    p = Process(target=mode_client, args=(self.__shared_nums,))
    p.start()
    self.__process = p
    return p
    
  def calculate(self, server: Server) -> None:
    super().calculate(server)
    self.__shared_nums[:] = []
    for num in server._nums:
      self.__shared_nums.append(num)
  
  def terminate(self) -> None:
    super().terminate()
    self.__process.terminate()