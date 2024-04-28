class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        counter = Counter(s)
        if c in counter:
            x = counter[c]
            return x * (x+1)//2
        return 0