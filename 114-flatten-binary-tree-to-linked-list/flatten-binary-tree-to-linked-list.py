# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        def dfs(root):
            if not root.left and not root.right:
                return root

            right = root.right
            if root.left:
                left = dfs(root.left)
                
                # Switch left pointer to right pointer
                root.right = root.left
                root.left = None
                left.right = right
            
            if right:
                return dfs(right)

            return left

        dfs(root)
            
        # set the left pointer and child pointer of the current root null
        # traverse to the left subtree
        # switch the left child to the right
        # set the right pointer of the new right child to point to the old right subtree
        