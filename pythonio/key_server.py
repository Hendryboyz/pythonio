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
  
  
  def __calculate(self):
    if self.__num_str != '':
      self.__append_number()
    print(self._nums)
    print(sum(self._nums))

  def add(self, client: Listener) -> None:
    super().add(client)
    self._listeners.append(client)
  
  def notify(self) -> None:
    super().notify()
    self.__calculate()
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
      
  def start(self):
    print('Server start to detect keyboard events')
    keyboard.wait()
