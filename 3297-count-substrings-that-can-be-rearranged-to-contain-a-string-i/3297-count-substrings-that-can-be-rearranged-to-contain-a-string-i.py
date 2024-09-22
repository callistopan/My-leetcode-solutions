class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        c = Counter(word2)
        total_unique = len(c)
        
        l = 0
        r = 0
        n = len(word1)
        current_unique = 0
        d = defaultdict(int)
        res = 0
        
        while r < n :
            d[word1[r]] += 1
            
            if word1[r] in c and d[word1[r]] == c[word1[r]]:
                current_unique += 1
            
            while current_unique == total_unique and l < n:
                res += n - r
                d[word1[l]] -= 1
                if word1[l] in c and d[word1[l]] < c[word1[l]]:
                    current_unique -= 1
                l += 1
            
            r += 1
        return res
                
                
        
        
        