# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dfs from root
        # rob1 -> rob2 -> current node
        # return max(rob1 + current node, rob2)
        # time: O(n)
        # space: O(n)

        def dfs(node):
            if not node:
                return (0, 0) # rob_this, skip_this

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            rob_this = node.val + left_skip + right_skip
            skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)

            return (rob_this, skip_this)
        
        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)
        