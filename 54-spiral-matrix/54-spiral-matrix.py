class Solution:
    '''time complexity=O(N*M) spacecomplexity=O(M*N)'''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        di=[0,1,0,-1]
        dj=[1,0,-1,0]
        res=[]
        visited={}
        i=0
        j=0
        d=0
        for k in range(n*m):
            res.append(matrix[i][j])
            visited[(i,j)]=1
            r=i+di[d]
            c=j+dj[d]
            if r>=0 and r<len(matrix) and c>=0 and c<len(matrix[0]) and (r,c) not in visited:
                i=r
                j=c
            else:
                d=(d+1)%4
                r=i+di[d]
                c=j+dj[d]
                i=r
                j=c
        return res