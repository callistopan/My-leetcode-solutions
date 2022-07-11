class Solution:
    def findCircleNum(self, M):
        
        n = len(M)
        ds = DisjointSet(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    ds.unite(i, j)
        return len(ds)
                
class DisjointSet:
    def __init__(self, n):
        self.cnt = n
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    
    def __len__(self):
        return self.cnt
    
    def find(self, p):
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def unite(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i != j:
            if self.rank[i] < self.rank[j]:
                i, j = j, i
            self.par[j] = i
            if self.rank[i] == self.rank[j]:
                self.rank[i] += 1
            self.cnt -= 1