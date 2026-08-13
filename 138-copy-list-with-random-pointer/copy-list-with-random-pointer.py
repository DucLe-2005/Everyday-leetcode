"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        old_to_new = {}
        old = head
        while old:
            if old not in old_to_new:
                old_to_new[old] = Node(old.val)
            new = old_to_new[old]
            
            if old.next:
                if old.next not in old_to_new:
                    old_to_new[old.next] = Node(old.next.val)
                new.next = old_to_new[old.next]

            if old.random:
                if old.random not in old_to_new:
                    old_to_new[old.random] = Node(old.random.val)
                new.random = old_to_new[old.random]

            old = old.next
        
        return old_to_new[head]
