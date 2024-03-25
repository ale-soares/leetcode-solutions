from typing import List

# Solution using reversed and more variables to improve readability
class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    car_fleets = []
    
    for p, s in reversed(sorted(pair)):
      car_arrival_time = (target - p) / s
      car_fleets.append(car_arrival_time)

      # if a car in the back takes the same amount of time or
      # less to arrive as the one in the front, they are a car fleet
      if len(car_fleets) >= 2 and car_fleets[-1] <= car_fleets[-2]:
        car_fleets.pop()

    return len(car_fleets)

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    stack = []
    
    for p, s in sorted(pair)[::-1]:  # Reverse Sorted Order
      stack.append((target - p) / s)
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()
    return len(stack)