class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        ones = 0
        zeros = 0
        l = 0
        for i in range(n):
            if s[i] == '0':
                zeros+= 1
            else:
                ones += 1
            while ones > k and zeros > k:
                if s[l] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                l += 1
            res += i - l + 1
        return res
