# User function Template for Python3

from collections import defaultdict,deque
class Solution:
    def minThrow(self, N, arr):
        # code here
        
        # push all special cells to dictionary
        
        d={}
        
        for i in range (0,2*N,2):
            
            d[arr[i]]= arr[i+1]
            
        # now make graph for every cell in the matrix
        
        graph = defaultdict(list)
        
        # there are 30 cells
        
        for cell in range(1,30):
            
            next_cell =cell+1
            
            while next_cell-cell <= 6 and next_cell <=30:
                
                # if this is a special cell
                
                if next_cell in d:
                    
                    graph[cell].append(d[next_cell])
                    
                else:  # normal cell
                
                    graph[cell].append(next_cell)
                    
                next_cell+=1
                
            
        # we taraverse the graph using bfs so that we can find the shortest distance
        
        # here the graph is not weighted so we can use BFS
        
        q= deque()
        
        q.append((1,0))  # node and distance
        
        
        while q:
            
            node ,distance = q.popleft()
            
            if node==30:
                return distance
            
            for neighbor in graph[node]:
                
                q.append((neighbor,distance+1))
                
        
        
        
                
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            
            

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends