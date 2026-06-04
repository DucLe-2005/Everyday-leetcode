# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0 # count edges

        def dfs(node):
            if not node:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_path = 0
            right_path = 0

            if node.left and node.left.val == node.val:
                left_path = left_len + 1
            if node.right and node.right.val == node.val:
                right_path = right_len + 1
            
            # path can bend through current node
            self.res = max(self.res, left_path + right_path)

            # parent can only continue one side
            return max(left_path, right_path)
    
        dfs(root)
        return self.res