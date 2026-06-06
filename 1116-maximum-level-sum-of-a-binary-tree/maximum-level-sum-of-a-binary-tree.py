# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        max_sum = float("-inf")
        q = deque([root])
        level = 1
        while q:
            sum = 0
            for _ in range(len(q)):
                node = q.popleft()  
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sum += node.val
            
            print(f"level {level}: {sum}")
            if sum > max_sum:
                print(f"{sum} > {max_sum}")
                res = level
                max_sum = sum
            level += 1
        
        return res