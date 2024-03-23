from collections import Counter

class Solution:
  # use counter1 to count the characters in s1
  # use counter2 for the same-length prefix of s2.
  # iterate a sliding window of length len(s1) across 2 and update ctr2
    # window always needs to have size of s1
  # if ever counter1 == counter2, return True; otherwise, return False

  def checkInclusion(self, s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    counter1, counter2 = Counter(s1), Counter(s2[:len1])  

    for index in range(len1, len2):
      if counter1 == counter2: return True

      counter2[s2[index - len1]] -= 1
      counter2[s2[index]] += 1

    return counter1 == counter2
  
class Solution:
  # does s2 have the same number of characters as s1
  # create a hashmap with the count of every character in the string s1
  # slide a window over the string s2 and decrease the counter for characters that occurred in the window
  # when all counters in the hashmap get to zero there is a permutation.

  def checkInclusion(self, s1: str, s2: str) -> bool:
    counter, window, matched = Counter(s1), len(s1), 0   

    for i in range(len(s2)):
      if s2[i] in counter: 
        counter[s2[i]] -= 1

        if counter[s2[i]] == 0:
            matched += 1

      if i >= window and s2[i - window] in counter: 
        if counter[s2[i - window]] == 0:
          matched -= 1

        counter[s2[i - window]] += 1

      if matched == len(counter):
        return True

    return False