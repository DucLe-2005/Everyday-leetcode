class MyHashMap:

    def __init__(self):
        self.keyRange = 769
        self.buckets = [Bucket() for _ in range(self.keyRange)]
    
    def _hash(self, key):
        print(f"key: {key}, hash: {key % self.keyRange}")
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        bucket.insertNode(key, value)

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        return bucket.getNode(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        bucket.deleteNode(key)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class Bucket:
    def __init__(self):
        self.head = Node(0, 0) # pseudo head
    
    def insertNode(self, key: int, val: int) -> None:
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.key == key:
                curr.val = val
                return
            curr = curr.next
            prev = prev.next
        prev.next = Node(key, val)

    def getNode(self, key: int) -> int:
        curr = self.head.next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def deleteNode(self, key: int) -> int:
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = prev.next
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)