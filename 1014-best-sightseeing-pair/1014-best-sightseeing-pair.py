class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        ans = A[0]
        prevBestIdx = 0
        for j in range(1,len(A)):
            ans = max(ans, A[prevBestIdx]+prevBestIdx+A[j]-j)
            if A[prevBestIdx] + prevBestIdx < A[j] + j:
                prevBestIdx = j
        return ans
                