class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for l in logs:
            if l =="../":
                ans = max(0,ans-1)
            elif l != "./":
                ans +=1
        return ans
                