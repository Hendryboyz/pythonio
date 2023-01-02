from pythonio.observers.interface import Listener, Server
from multiprocessing.process import BaseProcess
from multiprocessing import Process
from threading import Thread
from asyncio import AbstractEventLoop
import websockets
import asyncio
import json

async def mean(port: int):
  uri = f'ws://localhost:{port}'
  await asyncio.sleep(2)
  print('Client1 is ready')
  async for ws in websockets.connect(uri):
    try:
      async for nums_str in ws:
        nums = json.loads(nums_str)
        print(f'Client 1 received: {nums}')
        mean = sum(nums)/len(nums)
        print(f'Mean: {mean}')
    except:
      pass
    

def run_client_1(port: int):
  new_loop = asyncio.new_event_loop()
  new_loop.run_until_complete(mean(port))
  new_loop.run_forever()
  
class WebsocketListener(Listener):
  __CLIENTS: set
  __main_event_loop: AbstractEventLoop
  
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
    p = Process(target=run_client_1, args=(port,))
    p.start()
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
    def start_loop(new_loop, server):
      new_loop.run_until_complete(server)
      new_loop.run_forever()
    new_loop = asyncio.new_event_loop()
    start_server = websockets.serve(self.__handler, 'localhost', port, loop=new_loop)
    t = Thread(target=start_loop, args=(new_loop, start_server,))
    t.start()

  def __run(self, port: int = 8001):
    asyncio.run(self.__socket_server(port))