# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def recurse_tree(node):
            if not node or self.ans:
                return False
            
            left = recurse_tree(node.left)  # if p/q is in the left subtree
            right = recurse_tree(node.right)  # if p/q is in the right subtree

            mid = node == p or node == q

            if mid + left + right >= 2:  # LCA found if two flags are true
                self.ans = node
            
            return mid or left or right
        
        recurse_tree(root)
        return self.ans
