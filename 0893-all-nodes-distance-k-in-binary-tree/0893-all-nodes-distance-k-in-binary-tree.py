# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(current,parent):

            if current and parent:
                graph[current.val].append(parent.val)
                graph[parent.val].append(current.val)
            if current.left:
                build_graph(current.left,current)
            if current.right:
                build_graph(current.right,current)


        
        build_graph(root,None)

        # dfs
        seen = set()
        seen.add(target.val)
        answer = []

        def dfs(current,distance):

            if distance == k:
                answer.append(current)
                return 

            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor,distance + 1)
        dfs(target.val,0)
        return answer























