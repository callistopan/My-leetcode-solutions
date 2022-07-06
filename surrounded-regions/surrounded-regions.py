class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ''' add the boundary  'O's to the queue'''
        
        r=len(board)
        c=len(board[0])
        
        q=deque()  
        
        for i in range(r):
            if board[i][0]=='O':
                q.append((i,0))
            if board[i][c-1]=='O':
                q.append((i,c-1))
                
        for j in range(1,c-1):
            if board[0][j]=='O':
                q.append((0,j))
            if board[r-1][j]=='O':
                q.append((r-1,j))
                
        # mark all possible nodes which are 'O's as 'T'
        
        while  q:
            
            i,j = q.popleft()
            
            board[i][j] = 'T'
            dx=[1,-1,0,0]
            dy=[0,0,1,-1] 
            
            for d in range(4):
                n_x = i + dx[d]
                n_y = j + dy[d]
                
                if n_x >= 0 and n_x < r and n_y >= 0 and n_y < c and board[n_x][n_y]=='O':
                    
                    q.append((n_x,n_y))
                    
        # change all the 'O's still exists to 'X' and all the 'T's to 'O' s
        
        
        for i in range(r):
            
            for j in range(c):
                
                if board[i][j] == 'O':
                    board[i][j] ='X'
                    
                if board[i][j] == 'T':
                    board[i][j]='O'
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
                
        