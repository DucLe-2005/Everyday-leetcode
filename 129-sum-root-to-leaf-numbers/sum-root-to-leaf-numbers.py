# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, total):
            if not root.left and not root.right:
                return total * 10 + root.val
            
            total = total * 10 + root.val
            left = dfs(root.left, total) if root.left else 0
            right = dfs(root.right, total) if root.right else 0
            
            return left + right
        
        return dfs(root, 0)

            