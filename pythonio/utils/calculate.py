from typing import List
from collections import Counter

def mean(nums: List) -> float:
  return sum(nums) / len(nums)

def mode(nums: List) -> List:
  counters = Counter(nums)
  result = []
  for num, freq in counters.most_common():
    if len(result) > 0 and freq < counters[result[0]]:
      break
    result.append(num)
  return result
