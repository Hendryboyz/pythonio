from typing import List
import keyboard
from keyboard import KeyboardEvent
from pythonio.observers.interface import Server, Listener
import re

class KeyServer(Server):
  __num_str: str
  _nums: List[int]
  
  _listeners: List[Listener]
  
  def __init__(self) -> None:
    self.__num_str = ''
    self._listeners = []
    self._nums = []
    keyboard.add_hotkey('enter', self.notify)
    keyboard.add_hotkey('space', self.__append_number)
    keyboard.on_release(self.__press_hook)
  
  
  def add(self, client: Listener) -> None:
    super().add(client)
    self._listeners.append(client)
  
  def notify(self) -> None:
    super().notify()
    if self.__num_str != '':
      self.__append_number()
    for idx, client in enumerate(self._listeners):
      print(f'Notify listener[{idx}] - {client.name} to calculate')
      client.calculate(self)
    self._nums = []

  def __append_number(self):
    if self.__num_str == '':
      return
    self._nums.append(int(self.__num_str))
    self.__num_str = ''

  def __press_hook(self, event: KeyboardEvent):
    is_num = re.compile('\d+')
    if event.name != None and is_num.match(event.name):
      self.__num_str += event.name
    elif event.name == 'delete' and 0 < len(self.__num_str):
      self.__num_str = self.__num_str[:-1]
    else:
      pass
  
  def __shutdown_gracefully(self):
    for listener in self._listeners:
      listener.terminate()
  
  def start(self):
    print('Server is ready. You can type intergers and then click [ENTER] and press [Q]to exit.  Clients will show the mean, median, and mode of the input values.')
    keyboard.wait('Q')
    self.__shutdown_gracefully()
