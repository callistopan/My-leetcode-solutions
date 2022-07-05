"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        # bfs
        
        q= deque ([node])
        
        d={node:Node(node.val)}
        
        while q:
            
            v= q.popleft()
            
            for  u in v.neighbors:
                
                if u not in d:
                    
                    d[u] = Node(u.val)
                    
                    q.append(u)
                    
                d[v].neighbors.append(d[u])
                
        return  d[node]