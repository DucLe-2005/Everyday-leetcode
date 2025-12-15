# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # recursively travel each node
        # if a node's child is 1 more than the current node, then returb 1 + dfs(child's node)
        # if the node's child is not 1 more than the current node, then return dfs(child's node)
        # each call check if the current path is the longest Sequence

        self.longest_path = 0

        def dfs(node):
            if not node:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            current_len = 1 # at least the node itself
            
            if node.left and node.left.val == node.val + 1:
                current_len = max(current_len, 1 + left_len)
            
            if node.right and node.right.val == node.val + 1:
                current_len = max(current_len, 1 + right_len)
            
            self.longest_path = max(self.longest_path, current_len)

            return current_len
        
        dfs(root)
        return self.longest_path

