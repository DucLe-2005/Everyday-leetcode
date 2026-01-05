class LRUCache:
    # left <-> key1 (least recently used) <-> key2 <-> ... <-> key n (most recently used) <-> right
    # table: key: key, value: Node
    # capacity: capacity of table 
    class Node:
        def __init__(self, val=0, key=0):
            self.val = val
            self.key = key
            self.left, self.right = None, None
    
    def __init__(self, capacity: int):
        self.table = {}
        self.capacity = capacity
        self.head, self.tail = self.Node(), self.Node()
        self.head.right, self.tail.left = self.tail, self.head
        
    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        
        node = self.table[key]
        node.left.right, node.right.left = node.right, node.left
        self.move_right(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.table:
            node = self.table[key]
            node.val = value
            node.left.right, node.right.left = node.right, node.left
            self.move_right(node) 
        else:
            node = self.Node(key=key, val=value)
            self.table[key] = node
            self.move_right(node)
        
        if len(self.table) > self.capacity:
            self.remove_lru()
    
    def move_right(self, node):
        most_recently_used_node = self.tail.left
        most_recently_used_node.right = self.tail.left = node
        node.left, node.right = most_recently_used_node, self.tail
    
    def remove_lru(self):
        node = self.head.right
        self.head.right = node.right
        node.right.left = self.head
        del self.table[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)