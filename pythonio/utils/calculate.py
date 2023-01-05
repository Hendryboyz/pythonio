from typing import List
from collections import Counter

def mean(nums: List) -> float:
  return sum(nums) / len(nums)

def median(nums: List) -> float:
  nums.sort()
  if len(nums) & 1 == 1:
    return nums[len(nums)//2]
  else:
    mid_idx = int(len(nums)/2)
    return (nums[mid_idx] + nums[mid_idx - 1]) / 2

def mode(nums: List) -> List:
  counters = Counter(nums)
  result = []
  for num, freq in counters.most_common():
    if len(result) > 0 and freq < counters[result[0]]:
      break
    result.append(num)
  return result
