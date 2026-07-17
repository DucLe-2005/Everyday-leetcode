# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        def dfs(node, largest):
            nonlocal res
            if node.left:
                if node.left.val >= largest:
                    res += 1
                dfs(node.left, max(largest, node.left.val))
            if node.right:
                if node.right.val >= largest:
                    res += 1
                dfs(node.right, max(largest, node.right.val))
        
        dfs(root, root.val)
        return res
            
