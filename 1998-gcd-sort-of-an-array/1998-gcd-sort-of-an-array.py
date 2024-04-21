class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if u != self.parent.setdefault(u, u):
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv: self.parent[pu] = pv  #connect to the set,order doesnt matter


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def sieve(n):  # O(N*log(logN)) ~ O(N)
            spf = [i for i in range(n)]
            for i in range(2, n):
                if spf[i] != i: continue  # Skip if it's a not prime number
                for j in range(i * i, n, i):
                    if spf[j] > i:  # update to the smallest prime factor of j
                        spf[j] = i
            return spf

        def getPrimeFactors(num, spf):  # O(logNum)
            while num > 1:
                yield spf[num]
                num //= spf[num]

        spf = sieve(max(nums) + 1)  # find smallest prime factor for each number up to maximum
        print(spf)
        uf = UnionFind()
        for x in nums: # 10,5,9,3,15
            for f in getPrimeFactors(x, spf):
                uf.union(x, f)

        for x, y in zip(nums, sorted(nums)): #we are checking to the sorted,because the array can be already sorted
            if uf.find(x) != uf.find(y):
                return False

        return True