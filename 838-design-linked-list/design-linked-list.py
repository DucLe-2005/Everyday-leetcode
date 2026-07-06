class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.current_size = 0

    def get(self, index: int) -> int:
        if index >= self.current_size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        prev_head = self.head.next
        new_node = Node(val)
        self.head.next = new_node
        new_node.next = prev_head
        self.current_size += 1


    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val) 
        self.current_size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.current_size:
            return

        prev = self.head
        curr = self.head.next
        for _ in range(index):
            prev = curr
            curr = curr.next
        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr
        self.current_size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.current_size:
            return
        prev, curr = self.head, self.head.next
        for _ in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.current_size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)