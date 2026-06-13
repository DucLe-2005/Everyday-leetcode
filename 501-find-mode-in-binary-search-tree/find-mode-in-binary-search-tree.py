# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        values = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            values.append(node.val)  
            inorder(node.right)
        
        inorder(root)

        res = []
        max_freq = 0
        count = Counter(values)
        for num, freq in count.items():
            if freq > max_freq:
                res = [num]  
                max_freq = freq
            elif freq == max_freq:
                res.append(num)
        
        return res