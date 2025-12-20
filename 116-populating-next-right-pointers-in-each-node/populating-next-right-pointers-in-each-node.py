"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # queue: store the nodes
        # prev: store the previous node where we will connect prev.next = current_node
        # when processed all nodes in a level, reset prev = None
        if not root:
            return None

        q = deque([root])
        while q:
            prev = None
            for i in range(len(q)):
                cur = q.popleft()

                # Add children nodes to queue
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

                if prev:
                    prev.next = cur
                prev = cur
        
        return root
            
        
