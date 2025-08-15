class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev= None

class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.cap = capacity
        self.right = self.left = Node(0, 0)
        self.left.next = self.left.prev = self.right
        self.right.next = self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):  # insert to the left of the right most node
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.next = self.right
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
            self.insert(self.key_to_node[key])
            return self.key_to_node[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.remove(self.key_to_node[key])
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        self.insert(new_node)

        if len(self.key_to_node) > self.cap:
            del self.key_to_node[self.left.next.key]
            self.remove(self.left.next)
