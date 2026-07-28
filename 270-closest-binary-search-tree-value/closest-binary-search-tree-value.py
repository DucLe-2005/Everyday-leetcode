# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        min_diff = abs(root.val - target)
        def dfs(node):
            nonlocal res, min_diff
            if not node:
                return
            
            diff = abs(node.val - target)
            if diff == min_diff:
                res = min(node.val, res)
            elif diff < min_diff:
                res = node.val
                min_diff = diff

            if node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)
        
        dfs(root)
        return res