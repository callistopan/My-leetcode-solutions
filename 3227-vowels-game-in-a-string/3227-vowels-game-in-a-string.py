class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # poor bob
        t = "aeiou"
        for c in s:
            for v in t:
                if c == v:
                    return True
        return False