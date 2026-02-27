class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.cap = capacity
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        print("get key", key)
        if key in self.table:
            node = self.table[key]
            self.remove_node(node)
            self.move_right(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        print("put:", key, value)
        if key in self.table:
            node = self.table[key]
            node.val = value
            self.remove_node(node)
            self.move_right(node)
        else:
            print("new key:", key)
            new_node = Node(key, value)
            self.table[key] = new_node
            self.move_right(new_node)
            if len(self.table) > self.cap:
                print("len > capacity")
                self.remove_lru()
    
    def remove_node(self, node: Node):
        print(node.key)
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def move_right(self, node: Node):
        print("move right:", node.key)
        right_most = self.right.prev

        right_most.next = node
        node.next = self.right

        node.prev = right_most
        self.right.prev = node

    def remove_lru(self):
        print("remove_lru")
        node = self.left.next
        self.remove_node(node)
        del self.table[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)