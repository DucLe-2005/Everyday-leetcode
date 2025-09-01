# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_table = {}
        for i, val in enumerate(inorder):
            inorder_table[val] = i
        
        def array_to_tree(left, right):
            if left > right:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)

            root.right = array_to_tree(inorder_table[root_val] + 1, right)
            root.left = array_to_tree(left, inorder_table[root_val] - 1)

            return root
        
        return array_to_tree(0, len(postorder) - 1)