class MyHashMap:

    def __init__(self):
        self.size = 769
        self.buckets = [Bucket() for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        bucket.putNode(key, value)

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        return bucket.getNode(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        return bucket.removeNode(key)

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None

class Bucket:
    def __init__(self):
        self.head = Node() # pseudo head
    
    def putNode(self, key: int, val: int) -> None:
        prev, curr = self.head, self.head.next
        while curr:
            if curr.key == key:
                curr.val = val
                return
            curr = curr.next
            prev = prev.next
        
        # add new (key, value) pair since key is new
        prev.next = Node(key, val)
    
    def getNode(self, key: int) -> int:
        curr = self.head.next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
    
    def removeNode(self, key):
        prev, curr = self.head, self.head.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            curr = curr.next
            prev = prev.next
    



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)