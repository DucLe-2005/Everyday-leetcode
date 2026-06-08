# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(parent, node):
            if not node:
                if val < parent.val:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
                return
            
            if val < node.val:
                dfs(node, node.left)
            else:
                dfs(node, node.right)
            
        dfs(None, root)
        return root