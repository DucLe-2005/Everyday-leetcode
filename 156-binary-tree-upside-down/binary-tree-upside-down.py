# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left:
            return root

        def dfs(root, left, right):
            if not root:
                return None
            if not left:
                return root
        
            left_left = left.left
            left_right = left.right

            # change the order
            left.right = root
            left.left = right

            # turn upside down the left subtree

            return dfs(left, left_left, left_right)

        left = root.left
        right = root.right
        root.left = root.right = None

        return dfs(root, left, right)

