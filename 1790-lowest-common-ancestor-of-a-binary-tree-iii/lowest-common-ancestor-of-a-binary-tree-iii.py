"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path = set()
        while p:
            p_path.add(p.val)
            p = p.parent
        
        while q:
            if q.val in p_path:
                return q
            q = q.parent
