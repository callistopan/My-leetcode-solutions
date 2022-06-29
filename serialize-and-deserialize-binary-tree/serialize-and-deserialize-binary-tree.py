# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root == None: return "#"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right);

    def deserialize(self, data):
        nodes = data.split(",")
        self.i = 0

        def dfs():
            if self.i == len(nodes): 
                return None
            nodeVal = nodes[self.i]
            self.i += 1
            if nodeVal == "#": 
                return None
            
            root = TreeNode(int(nodeVal))
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))