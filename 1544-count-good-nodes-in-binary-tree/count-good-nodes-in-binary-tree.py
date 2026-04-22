# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, max_num):
            if not root:
                return
            if root.val >= max_num:
                self.res += 1
            max_num = max(root.val, max_num)
            dfs(root.left, max_num)
            dfs(root.right, max_num)
        
        dfs(root, root.val)
        return self.res