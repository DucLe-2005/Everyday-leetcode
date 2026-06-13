# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        curr_count = 0
        mode = []
        max_freq = 0
        count = 0
        curr = root
        stack = []
        prev_val = float("-inf")

        while curr or stack:
            while curr:
                stack.append(curr)  
                curr = curr.left
            
            node = stack.pop()  
            if node.val == prev_val:
                count += 1
            else:
                count = 1
            
            if count > max_freq:
                max_freq = count
                mode = [node.val]  
            elif count == max_freq:
                mode.append(node.val)  
            
            prev_val = node.val
            curr = node.right

        return mode