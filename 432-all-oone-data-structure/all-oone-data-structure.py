class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.left = self.right = None

    def add(self, key):
        self.keys.add(key)

    def remove(self, key):
        self.keys.remove(key)

class AllOne:
    # head <-> min key <-> key2 <-> key3 <-> ... <-> max key <-> tail
    # how do I make sure that the linked list is sorted?

    def __init__(self):
        self.count_map = {}
        self.head, self.tail = Node(0), Node(-1)
        self.head.right, self.tail.left = self.tail, self.head

    def insert_right(self, key, prev_node):
        if prev_node.right.count == prev_node.count + 1:
            nxt_node = prev_node.right
            nxt_node.add(key)
            self.count_map[key] = nxt_node
        else:
            new_node = Node(prev_node.count + 1)
            new_node.add(key)
            new_node.right, new_node.left = prev_node.right, prev_node
            prev_node.right.left = new_node
            prev_node.right = new_node
            self.count_map[key] = new_node

    def insert_left(self, key, prev_node):
        if prev_node.left.count == prev_node.count - 1:
            left_node = prev_node.left
            left_node.add(key)
            self.count_map[key] = left_node
        else:
            new_node = Node(prev_node.count - 1)
            new_node.add(key)
            new_node.right, new_node.left = prev_node, prev_node.left
            prev_node.left.right = new_node
            prev_node.left = new_node
            self.count_map[key] = new_node
    
    def remove_node(self, node):
        node.left.right, node.right.left = node.right, node.left

    def inc(self, key: str) -> None:
        if key in self.count_map:
            node = self.count_map[key]
            node.remove(key)
            self.insert_right(key, node)
            if len(node.keys) == 0:
                self.remove_node(node)
        else:
            self.insert_right(key, self.head)

    def dec(self, key: str) -> None:
        node = self.count_map[key]
        node.remove(key)

        if node.count == 1:
            del self.count_map[key]
        else:
            self.insert_left(key, node)
            
        if len(node.keys) == 0:
            self.remove_node(node)

    def getMaxKey(self) -> str:
        if not self.tail.left.keys:
            return ""
        key = self.tail.left.keys.pop()
        self.tail.left.add(key)
        return key

    def getMinKey(self) -> str:
        if not self.head.right.keys:
            return ""
        key = self.head.right.keys.pop()
        self.head.right.keys.add(key)
        return key
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()