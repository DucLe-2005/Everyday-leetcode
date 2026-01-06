# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if either p or q is higher and lower than root, the root is the lCU  
        # if both p and q are lower than root, then move the root pointer to the left
        # if both p and q are higher than root, then move the root pointer to the right
        # if the current root is equal to either p or q, then current root is the lCU

        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root