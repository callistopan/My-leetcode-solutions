class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        if not grid or not grid[0]:
            return False

        m, n = len(grid), len(grid[0])
        
        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        # Initialize visited matrix with -1
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Initial health after stepping on (0,0)
        initial_health = health - grid[0][0]
        if initial_health <=0:
            return False
        visited[0][0] = initial_health
        
        queue = deque()
        queue.append( (0,0, initial_health) )
        
        while queue:
            x, y, current_health = queue.popleft()
            
            # If reached the end
            if x == m-1 and y == n-1:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check boundaries
                if 0 <= nx < m and 0 <= ny < n:
                    # Calculate new health
                    new_health = current_health - grid[nx][ny]
                    
                    if new_health <=0:
                        continue
                    # If we have not visited this cell, or have more health now
                    if new_health > visited[nx][ny]:
                        visited[nx][ny] = new_health
                        queue.append( (nx, ny, new_health) )
        
        return False