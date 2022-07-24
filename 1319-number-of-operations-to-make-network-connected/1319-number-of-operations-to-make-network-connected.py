class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''As long as there are at least (n - 1) connections, there is definitely a way to connect all computers.'''
        if len(connections)<n-1:
            return -1
        
        # find isolated computer clusters
        
        graph = defaultdict(list)
        
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            
        # do dfs to find isolated clusters
        
        count=0
        visited={}
        for v in range(n):
            
            if v not in graph:
                count+=1
            
            elif v not in visited:
                
                self.dfs(graph,v,visited)
                
                count+=1
            
                
        return count-1
    
    
    def dfs(self,graph,v,visited):
        
        visited[v]=True
        
        for u in graph[v]:
            if u not in visited:
                self.dfs(graph,u,visited)
        
            
        