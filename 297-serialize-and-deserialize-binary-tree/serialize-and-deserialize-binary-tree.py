# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = []
        def dfs(root):
            if not root:
                res.append("None")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        print(",".join(res))
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        s = data.split(",")
        size = len(s)
        self.index = 0

        def dfs(s):
            if self.index >= size or s[self.index] == 'None':
                self.index += 1
                return None
            
            root = TreeNode(s[self.index])
            self.index += 1
            root.left = dfs(s)
            root.right = dfs(s)

            return root
        
        return dfs(s)
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))