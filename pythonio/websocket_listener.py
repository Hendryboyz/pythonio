from pythonio.observers.interface import Listener, Server
from multiprocessing.process import BaseProcess
from multiprocessing import Process
from threading import Thread
from asyncio import AbstractEventLoop
from pythonio.utils.calculate import mean
import websockets
import asyncio
import json

async def calculate_mean(port: int):
  uri = f'ws://localhost:{port}'
  await asyncio.sleep(2)
  print('Client1 is ready')
  async for ws in websockets.connect(uri):
    try:
      async for nums_str in ws:
        nums = json.loads(nums_str)
        numsMean = mean(nums)
        print(f'Mean is	{numsMean}')
    except:
      pass
    

def mean_client(port: int):
  client_loop = asyncio.get_event_loop()
  client_loop.run_until_complete(calculate_mean(port))
  client_loop.run_forever()
  
def socket_server(loop, server):
  asyncio.set_event_loop(loop)
  loop.run_until_complete(server)
  loop.run_forever()
  
class WebsocketListener(Listener):
  __CLIENTS: set
  __main_event_loop: AbstractEventLoop
  __process: BaseProcess
  __server_event_loop: AbstractEventLoop
  
  def __init__(self, name: str) -> None:
    super().__init__(name)
    self.__CLIENTS = set()
  
  async def __send_clients(self, nums):
    print(f'Send to clients: {nums}')
    for websocket in self.__CLIENTS.copy():
      try:
        await websocket.send(json.dumps(nums))
      except websockets.ConnectionClosed:
        pass
  
  def calculate(self, server: Server) -> None:
    super().calculate(server)
    self.__main_event_loop.run_until_complete(self.__send_clients(server._nums))
    
  def start(self) -> BaseProcess:
    super().start()
    port = 3000
    self.__main_event_loop = asyncio.get_event_loop()
    self.__run(port)
    p = Process(target=mean_client, args=(port,))
    p.start()
    self.__process = p
    return p
  
  async def __handler(self, websocket):
    self.__CLIENTS.add(websocket)
    print(f'Current clients count: {len(self.__CLIENTS)}')
    try:
      await websocket.wait_closed()
    finally:
      self.__CLIENTS.remove(websocket)
  

  async def __socket_server(self, port: int = 8001) -> None:
    print(f'start socket server on port[{port}]')
    
    server_loop = asyncio.new_event_loop()
    self.__server_event_loop = server_loop
    
    start_server = websockets.serve(self.__handler, 'localhost', port, loop=server_loop)
    t = Thread(target=socket_server, args=(server_loop, start_server,))
    t.start()

  def __run(self, port: int = 8001):
    asyncio.run(self.__socket_server(port))
  
  def terminate(self) -> None:
    super().terminate()
    print('socket terminate')
    for client in self.__CLIENTS:
      self.__main_event_loop.create_task(client.close())
    self.__server_event_loop.stop()
    self.__process.terminate()