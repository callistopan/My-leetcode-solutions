class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        c = 0
        for word in words:
            f = 1
            for cu in word:
                if cu not in allowed:
                    f = 0
                    break
            if f:
                c += 1
        return c