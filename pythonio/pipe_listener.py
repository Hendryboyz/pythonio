from pythonio.observers.interface import Listener, Server
from multiprocessing.process import BaseProcess
from multiprocessing.connection import Connection
from multiprocessing import Process, Pipe

def median_client(conn: Connection):
  print('Client2 is ready')
  while True:
    nums = conn.recv()
    nums = sorted(nums)
    if len(nums) & 1 == 1:
      print(f'Meidan is {nums[len(nums)//2]}')
    else:
      mid_idx = int(len(nums)/2)
      median = (nums[mid_idx] + nums[mid_idx - 1]) / 2
      print(f'Median is {median}')

class PipeListener(Listener):
  __conn: Connection = None
  __process: BaseProcess = None
  
  def __init__(self, name: str) -> None:
    super().__init__(name)
    
  def start(self) -> BaseProcess:
    super().start()
    receiver_conn, sender_conn = Pipe()
    self.__conn = sender_conn
    p = Process(target=median_client, args=(receiver_conn,))
    p.start()
    self.__process = p
    return p
    
  def calculate(self, server: Server) -> None:
    super().calculate(server)
    self.__conn.send(server._nums)
  
  def terminate(self) -> None:
    super().terminate()
    self.__conn.close()
    self.__process.terminate()
    