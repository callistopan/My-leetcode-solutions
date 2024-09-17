class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        c1 = Counter(s1)
        c2 = Counter(s2)
        c = c1 + c2
        
        res = []
        for k,v in c.items():
            if v == 1:
                res.append(k)
        return res