class MyHashSet:
    # time: O(N/K), N = # of keys, K = # of buckets
    # space: O(N + K)

    def __init__(self):
        self.keyRange = 769 # prime number for less collision
        self.buckets = [Bucket() for _ in range(self.keyRange)]
        
    def _hash(self, val):
        return val % self.keyRange

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        bucket.insert(key)  

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        bucket.delete(key)

    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        return bucket.exists(key)

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class Bucket:
    def __init__(self):
        self.head = Node(0) # pseudo head
    
    def insert(self, val):
        if self.exists(val):
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def exists(self, val):
        curr = self.head.next
        while curr:
            if curr.val == val:
                return True
            curr = curr.next

        return False
    
    def delete(self, val):
        if not self.exists(val):
            return
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.val == val:        
                prev.next = curr.next
                return
            prev = prev.next
            curr = curr.next

            

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)