# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root
        def dfs(root):
            if not root:
                return False
            
            mid = root.val == p.val or root.val == q.val
            left = dfs(root.left)
            right = dfs(root.right)

            if (left and right) or (mid and left) or (mid and right):
                self.res = root
                
            return mid or left or right

        dfs(root)
        return self.res