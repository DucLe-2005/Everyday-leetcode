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
        q = deque([root])
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    res.append("None")
                    continue
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)

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
        root = TreeNode(s[0])
        q = deque([root])
        idx = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue

                if idx + 1 < size and s[idx + 1] != "None":
                    node.left = TreeNode(int(s[idx + 1]))
                else:
                    node.left = None
                
                if idx + 2 < size and s[idx + 2] != "None":
                    node.right = TreeNode(int(s[idx + 2]))
                else:
                    node.right = None
                
                q.append(node.left)
                q.append(node.right)

                idx += 2

                if not root:
                    root = node
        
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))