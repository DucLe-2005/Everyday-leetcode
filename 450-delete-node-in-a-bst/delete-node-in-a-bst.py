# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = self.findPredecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = self.findSuccessor(root)
                root.right = self.deleteNode(root.right, root.val)
        
        return root
    def findPredecessor(self, node):
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr.val

    def findSuccessor(self, node):
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr.val