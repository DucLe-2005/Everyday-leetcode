# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root is p or q and found p or q on either left or right child: root is lca
        # if root is not p or q and found p or q on both or right child: root is lca
        res = None

        def dfs(node):
            nonlocal res
            if not node or res:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            x = left + right
            if node.val == p.val or node.val == q.val:
                x += 1
            
            if x == 2 and not res:
                res = node

            return x
        
        dfs(root)
        return res