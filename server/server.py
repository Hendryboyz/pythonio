from typing import List
import keyboard
from keyboard import KeyboardEvent
import re

class KeyServer:
  __num_str: str
  __nums: List
  
  def __init__(self) -> None:
    self.__num_str = ''
    self.__nums = []
    keyboard.add_hotkey('enter', self.calculate)
    keyboard.add_hotkey('space', self.append_number)
    keyboard.on_release(self.press_hook)
    
  def calculate(self):
    if self.__nums != '':
      self.append_number()
    print(self.__nums)
    print(sum(self.__nums))

  def append_number(self):
    if self.__nums == '':
      return
    self.__nums.append(int(self.__num_str))
    self.__num_str = ''

  def press_hook(self, event: KeyboardEvent):
    is_num = re.compile('\d+')
    if event.name != None and is_num.match(event.name):
      self.__num_str += event.name
      
  def start(self):
    keyboard.wait()