from collections import defaultdict
from typing import List

# Solution using sort | O(m * n log n)
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    
    for word in strs:
      sorted_word = ''.join(sorted(word))
      anagram_map[sorted_word].append(word)
  
    return list(anagram_map.values())

# Non-sort solution | O(m * n) - m: total number of input strings, n: average length of string
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # counts how many of each letter there are per word using an array of 26 elements (lowercase a to lowercase z)
    # ex: eat -> count = [a:1, b:0, c:0, d:0, e: 1, f:0, g:0...t:1...z:0]
    # every word that shares the same letters in the same quantity gets grouped together
    # ex: [count]: ["eat", "ate", "tea"]

    # using default dict in case to deal with non existing keys
    ans = defaultdict(list)

    for s in strs:
      # creates a list of 26 0s corresponding to a...z
      count = [0] * 26

      for c in s:
        # count how many of each char in the string
        # maps a to index 0 and z to index 25
        # ord(x) get ascii value of x
        # increment by one to count how many of each char there is
        count[ord(c) - ord("a")] += 1

      # groups all anagrams with this particular count together
      # change to tuple because in python lists cannot be keys, tuples are non mutable
      ans[tuple(count)].append(s)

    # returns just the keys, because they contain a list of words that are anagrams
    return ans.values()