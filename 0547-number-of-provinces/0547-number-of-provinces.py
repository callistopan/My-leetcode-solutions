class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        v =len(isConnected)
        visited ={}
        count=0
        for i in range(v):
            
            if i not in visited:
                count+=1
                self.dfs(i,isConnected,visited)
                
        return count
                
    
    def dfs(self,v,graph,d):
        
        if v in d:
            return 
        
        d[v]=True
        
        for i in range(len(graph)):
            
            if i!=v and graph[v][i]==1:
                
                self.dfs(i,graph,d)
        
        
            