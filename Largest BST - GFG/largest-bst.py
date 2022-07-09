#User function Template for python3

class NodeInfo:
    def __init__(self):
        
        self.min = float("inf")
        self.max= float("-inf")
        self.isBST=True
        self.size=0
        
class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        #code here
        return self.largest(root).size
        
    def largest(self,root):
        
        if not root:
            return NodeInfo()
            
        left = self.largest(root.left)
        
        right = self.largest(root.right)
        
        m = NodeInfo()
        
        if not left.isBST  or not right.isBST or left.max >=root.data or right.min <= root.data:
            m.isBST=False
            
            m.size= max(left.size,right.size)
            return m
            
        m.isBST= True
        
        m.size=left.size+right.size+1
        
        m.min= left.min if root.left else root.data
        
        m.max= right.max if root.right else root.data
        
        return m

#{ 
#  Driver Code Starts
import sys
sys.setrecursionlimit(1000000)

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root



if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()

        root = buildTree(s)
        ob = Solution()
        print(ob.largestBst(root))

# } Driver Code Ends