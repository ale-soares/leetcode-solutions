from typing import List

# Time complexity: O(n), Space complexity: O(1)
class Solution:
  def encode(self, strs: List[str]) -> str:
    encoded = ""

    # for input ["neet","code","love","you"]
    # encoded pattern will be "4#neet4#code4#love3#you"
    for s in strs:
      encoded += str(len(s)) + "#" + s

    return encoded

  def decode(self, s: str) -> List[str]:
    decoded, i = [], 0

    while i < len(s):
      j = i

      # while at an integer character
      # gets the integer portion of encoded string to get its length
      while s[j] != "#":
        j += 1
      
      # for segment "4#neet", first char is n and length of word is 4
      first_char = j
      st_length = int(s[i : first_char])
      # use word length (4) to find its last char
      last_char = first_char + 1 + st_length

      # append word "neet"
      decoded.append(s[first_char + 1 : last_char])
      i = last_char

    return decoded
