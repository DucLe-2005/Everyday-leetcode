# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_values = []
        self.getBSTNodes(root, node_values)
        print(node_values)
        return self.createTree(node_values, 0, len(node_values) - 1)
    
    def getBSTNodes(self, root, res):
        if not root:
            return
        
        self.getBSTNodes(root.left, res)
        res.append(root.val)
        self.getBSTNodes(root.right, res)
    
    def createTree(self, values, l, r):
        print(f"l: {l}, r: {r}")
        if l > r:
            return None
        m = (l + r) // 2
        root = TreeNode(values[m])
        root.left = self.createTree(values, l, m - 1)
        root.right = self.createTree(values, m + 1, r)

        return root
