class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts=Counter(text)
        result=float("inf")
        print(counts)
        for c ,count in Counter('balloon').items():
            result=min(result,counts[c]//count)
            
        return result