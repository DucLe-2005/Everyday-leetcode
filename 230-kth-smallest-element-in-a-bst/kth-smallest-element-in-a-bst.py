# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive inorder traversal
        # def inorder(root):
        #     if root:
        #         return inorder(root.left) + [root.val] + inorder(root.right)
        #     else:
        #         return []
        
        # return inorder(root)[k-1]

        # iterative inorder traversal
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right