class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hashTable ={}
        
        for a in A:
            for b in B:
                if a+b in hashTable:
                    hashTable[a+b] += 1
                else:
                    hashTable[a+b] = 1
                    
        result = 0
        for c in C:
            for d in D:
                if -(c+d) in hashTable:
                    result += hashTable[-(c+d)]
        return result
        