import multiprocessing as mp
import websockets
import asyncio
from queue import Queue
from multiprocessing.process import BaseProcess
from key import KeyServer

async def echo(websocket):
  async for message in websocket:
    await websocket.send(message)

async def socket_server(port: int = 8001) -> None:
  print(f'start socket server on port[{port}]')
  async with websockets.serve(echo, 'localhost', port):
    await asyncio.Future()

def start(q: Queue, port: int = 8001):
  asyncio.run(socket_server(port))
  
def main():
  socket_ctx = mp.get_context('spawn')
  q = socket_ctx.Queue()
  p = socket_ctx.Process(target=start, args=(q, 3000))
  p.start()
  server = KeyServer()
  server.start()
  p.join()
  

if __name__ == '__main__':
  main()