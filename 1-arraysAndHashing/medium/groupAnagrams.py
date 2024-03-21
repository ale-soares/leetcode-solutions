from collections import defaultdict
from typing import List

# Solution using sort
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    
    for word in strs:
      sorted_word = ''.join(sorted(word))
      anagram_map[sorted_word].append(word)
  
    return list(anagram_map.values())

# Non-sort solution
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)

    for s in strs:
      count = [0] * 26
      for c in s:
        count[ord(c) - ord("a")] += 1
      ans[tuple(count)].append(s)
    return ans.values()