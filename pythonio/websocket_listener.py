from pythonio.observers.interface import Listener, Server

class WebsocketListener(Listener):
  def __init__(self, name: str) -> None:
    super().__init__(name)
  
  def calculate(self, server: Server) -> None:
    super().calculate(server)
    print('Mean:', sum(server._nums)/len(server._nums))