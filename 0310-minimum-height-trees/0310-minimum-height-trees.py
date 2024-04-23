class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''find the two centroids if possible '''
        if n<=2:
            # edge case
            return [i for i in range(n)]
        #build graph
        neighbors=[set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        
        #first layer of leaves
        leaves=[]
        for i in range(n):
            if len(neighbors[i])==1: #only one adjacent node for  this node
                leaves.append(i)
                
        remaining_nodes=n
        #now trim alll nodes
        while remaining_nodes >2:
            remaining_nodes-=len(leaves)
            new_leaves=[]
            
            while leaves:
                leaf=leaves.pop()
                neighbor=neighbors[leaf].pop()
                #remove edge to leaf node
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor])==1:
                    new_leaves.append(neighbor)
            leaves=new_leaves
            
        return leaves