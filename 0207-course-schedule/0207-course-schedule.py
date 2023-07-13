class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph=[[] for i in range(numCourses)]
        visited=[False for i in range(numCourses)]
        stack=[False for i in range(numCourses)]
        for pair in prerequisites:
            x,y=pair
            graph[x].append(y)   ###simply making graph
        
        
        for course in range(numCourses):
            if visited[course]==False:
                if self.dfs(graph,visited,stack,course):
                    return False
        return True
    
    
    
    def dfs(self,graph,visited,stack,course):#####detect cycle   checks if a given nodes dfs search has any nodes that has edge to selected node if yes return True
            visited[course]=True
            stack[course]=True

            for neigh in graph[course]:
                if visited[neigh]==False:
                    if self.dfs(graph,visited,stack,neigh):
                        return True

                elif stack[neigh]:###already visited
                    return True
            stack[course]=False
            return False