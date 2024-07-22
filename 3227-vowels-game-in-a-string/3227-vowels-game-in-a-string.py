class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # poor bob
        t = "aeiou"
        for c in s:
            if c in t:
                return True
        return False