class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0 for i in range(n)] for j in range(n)]
        
        i=0
        j=0
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        dr=0
        number=1
        while number<=n**2:    
            m[i][j]=number
            number+=1
            r=i+dx[dr]
            c=j+dy[dr]
            if r>=0 and r<len(m) and c>=0 and c<len(m[0]) and m[r][c]==0:
                    
                i=r
                j=c
            
                
            else:
                dr=(dr+1)%4
                r=i+dx[dr]
                c=j+dy[dr]
                i=r
                j=c
        return m
            