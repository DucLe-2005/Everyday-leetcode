class Node:
    def __init__(self, count: int):
        self.keys = set()
        self.count = count
        self.prev, self.next = None, None

    def add(self, key: str):
        self.keys.add(key)

    def remove(self, key: str):
        self.keys.remove(key)

class AllOne:

    def __init__(self):
        self.countMap = {}  # key -> Node
        self.left, self.right = Node(0), Node(float("inf"))
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.countMap:
            node = self.countMap[key]
            count = node.count + 1
            next_node = node.next  # Fix: cache before removing node
            node.remove(key)
            if len(node.keys) == 0:
                self.remove(node)
                node = node.prev
        else:
            node = self.left
            count = 1
            next_node = self.left.next

        if next_node.count != count:
            new_node = Node(count)
            self.insert(new_node, node)
            next_node = new_node
        next_node.add(key)
        self.countMap[key] = next_node


    def dec(self, key: str) -> None:
        node = self.countMap[key]
        count = node.count - 1
        node.remove(key)

        if count == 0:
            del self.countMap[key]
        else:
            prev_node = node.prev
            if prev_node.count != count:
                new_node = Node(count)
                self.insert(new_node, prev_node)
                prev_node = new_node
            prev_node.add(key)
            self.countMap[key] = prev_node

        if len(node.keys) == 0:
            self.remove(node)

    def getMinKey(self) -> str:
        node = self.left.next
        if node == self.right:
            return ""
        return next(iter(node.keys))  # get an arbitrary key

    def getMaxKey(self) -> str:
        node = self.right.prev
        if node == self.left:
            return ""
        return next(iter(node.keys))  # get an arbitrary key
