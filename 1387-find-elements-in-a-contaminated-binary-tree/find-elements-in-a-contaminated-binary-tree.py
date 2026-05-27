# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    # init:
    # time: O(n)
    # space: O(n)

    # find:
    # time: O(n)
    # space: O(n)
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.build_tree(self.root)
        
    def build_tree(self, root):
        if not root:
            return
        if root.left:
            root.left.val = 2 * root.val + 1
            self.build_tree(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.build_tree(root.right)


    def find(self, target: int) -> bool:
        def dfs(root):
            if not root:
                return False
            
            if root.val == target:
                return True

            return dfs(root.left) or dfs(root.right)
        
        return dfs(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)