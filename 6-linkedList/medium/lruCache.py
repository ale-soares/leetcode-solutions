class Node:
  def __init__(self, key, value):
    self.key, self.value = key, value
    self.prev = self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.cap = capacity
    # cache is a HM that maps a key to a node
    self.cache = {}

    # left is least recent value added and right is most recent
    self.left, self.right = Node(0, 0), Node(0, 0)
    # connect left and right to put new nodes in between
    self.left.next, self.right.prev = self.right, self.left

  def remove(self, node):
    prev, nxt = node.prev, node.next
    prev.next, nxt.prev = nxt, prev

  def insert(self, node):
    prev, nxt = self.right.prev, self.right
    prev.next = nxt.prev = node
    node.next, node.prev = nxt, prev

  def get(self, key: int) -> int:
    if key in self.cache:
      # update value to be most recent in the list (remove and insert at rightmost position)
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].value

    return -1

  def put(self, key: int, value: int) -> None:
    # if a node with the same key is already in cache, it needs to be removed before new one is added
    if key in self.cache:
      self.remove(self.cache[key])

    self.cache[key] = Node(key, value)
    self.insert(self.cache[key])

    # if new value addition goes above the cap, remove the least used node (next to leftmost pointer)
    if len(self.cache) > self.cap:
      lru = self.left.next
      self.remove(lru)
      del self.cache[lru.key]