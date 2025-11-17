"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. iterate each node
        # 2. if node has a child, call a function to change the child node to be in the next pointer of the current node
        # 3. the helper function returns the end of the linked list
        # 4. base case: return the end node of a linked list
        # 5. relink the new end
        def dfs(node):
            prev = None
            while node:
                if node.child:
                    nxt = node.next
                    child_tail = dfs(node.child)
                    
                    # Reconnect child
                    node.next = node.child
                    node.next.prev = node
                    node.child = None
                    
                    if nxt:
                        child_tail.next = nxt
                        nxt.prev = child_tail
                    
                    
                prev = node
                node = node.next

            return prev
            
        dfs(head)
        return head




         