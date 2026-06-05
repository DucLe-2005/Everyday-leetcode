# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root, sum):
            if not root:
                return
            sum <<= 1
            sum += root.val
            if not root.left and not root.right:
                self.res += sum
                return
            dfs(root.left, sum)
            dfs(root.right, sum)
        
        dfs(root, 0)
        return self.res

            