# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if current node is between p and q, return current node
        # if current node is bigger than p and q, find common ancestor on root.left 
        # if current node is smaller than p and q, find common ancestor on root.right  
        # if current node is p or q, return the current node

        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
