# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        trees = []
        to_delete = set(to_delete)
        
        def dfs(node, parent, child):
            if not node:
                return
            
            print(f"node: {node.val}, parent: {parent.val}")
            if node.val in to_delete:
                if child == 0:
                    parent.left = None
                else:
                    parent.right = None
            else:
                if parent.val in to_delete:
                    trees.append(node)
            
            dfs(node.left, node, 0)
            dfs(node.right, node, 1)

        pop = to_delete.pop()
        to_delete.add(pop)
        dfs(root, TreeNode(pop), 0)
        return trees