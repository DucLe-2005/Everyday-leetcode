# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        i = 0

        def dfs(root, i):
            if not root:
                return i
            left = dfs(root.left, i+1)
            right = dfs(root.right, i+1)
            return max(left, right)
        
        return dfs(root, i)