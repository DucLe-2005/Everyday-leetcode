# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # time: O(logN) in a balanced BST, O(n) in a totally skewed tree
        # space: O(logN)................., O(n) in a skewed tree
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # node is a leaf
            if not root.left and not root.right:
                root = None
            elif root.right: # node has a right child
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val) # delete the selected leaf
            else: # node has a left childe
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val) # delete the selected leaf

        return root

    def predecessor(self, node):
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr.val
    
    def successor(self, node):
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr.val
    
