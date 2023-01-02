from pythonio.key_server import KeyServer
from pythonio.websocket_listener import WebsocketListener
from pythonio.pipe_listener import PipeListener
# from pythonio.shared_memory_listener import SharedMemoryListener

def main():
  client1 = WebsocketListener('websocket')
  client2 = PipeListener('pipe')
  # client3 = SharedMemoryListener('shared-memory')
  
  p1 = client1.start()
  p2 = client2.start()
  # p3 = client3.start()
  
  server = KeyServer()
  server.add(client1)
  server.add(client2)
  # server.add(client3)
  server.start()
  
  p1.join()
  p2.join()
  # p3.join()
  

if __name__ == '__main__':
  main()