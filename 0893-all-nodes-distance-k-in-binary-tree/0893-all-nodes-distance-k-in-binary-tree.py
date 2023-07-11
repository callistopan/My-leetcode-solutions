# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list) # graph

        def build_graph(current,parent):

            if current and parent:  # current node has a parent
                graph[current.val].append(parent.val)
                graph[parent.val].append(current.val)
            if current.left: # has a left child , recurse for that node
                build_graph(current.left,current)
            if current.right: # has a right chilid, recurse for that node
                build_graph(current.right,current)


        
        build_graph(root,None)

        # dfs
        seen = set() # for storing visited nodes 
        seen.add(target.val)
        answer = []

        def dfs(current,distance):

            if distance == k: # distance k from target
                answer.append(current)
                return 

            for neighbor in graph[current]: # visit all neighbor node
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor,distance + 1)
        dfs(target.val,0)
        return answer























