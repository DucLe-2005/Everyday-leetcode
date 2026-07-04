class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.pairs = {}
        self.left, self.right = Node(), Node() 
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
    
    def _delete_node(self, node):
        node_left, node_right = node.prev, node.next
        node_left.next = node_right
        node_right.prev = node_left

    def _move_leftmost(self, node):
        nxt = self.left.next
        node.prev, node.next = self.left, nxt
        self.left.next = node
        nxt.prev = node   

        
    def get(self, key: int) -> int:
        if key in self.pairs:
            node = self.pairs[key]
            self._delete_node(node)
            self._move_leftmost(node)
            return node.val
        return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            node = self.pairs[key]
            node.val = value
            self._delete_node(node)
            self._move_leftmost(node)
        else:
            node = Node(key, value)
            self.pairs[key] = node
            self._move_leftmost(node)

            if len(self.pairs) > self.capacity:
                del self.pairs[self.right.prev.key]
                self._delete_node(self.right.prev)
            
    def _print_list(self):
        curr = self.left.next
        res = []

        while curr != self.right:
            res.append(f"{curr.key}: {curr.val}")
            curr = curr.next

        return " -> ".join(res)
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)