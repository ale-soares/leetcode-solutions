from collections import defaultdict
from typing import List

# Solution using regular dictionary
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = {}

    for num in nums:
      if num in counter:
        counter[num] += 1
      else:
        counter[num] = 1
    
    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    return list(counter.keys())[:k]

# Solution using default dict
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    num_freq_map = defaultdict(int)

    for num in nums:
      num_freq_map[num] += 1
    
    sorted_nums_per_freq = [key for key, val in sorted(num_freq_map.items(), key = lambda item: -item[1])]
    return sorted_nums_per_freq[:k]

# Solution using default dict and simpler sort with shorter return
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = defaultdict(int)

    for number in nums:
      counter[number] += 1

    return sorted(counter, key=counter.get, reverse=True)[:k]