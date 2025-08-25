# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            parent_val = root.val
            if p.val > parent_val and q.val > parent_val:
                root = root.right
            elif p.val < parent_val and q.val < parent_val:
                root = root.left
            else:
                return root
