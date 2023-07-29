class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def maxDiff(left,right):
            if (left,right) in memo:
                return memo[(left,right)]
            if left == right:
                return nums[left]
            score_by_left = nums[left] - maxDiff(left+1 , right) # other player plays optimally
            score_by_right = nums[right] - maxDiff(left, right-1)

            memo[(left,right)] = max(score_by_left, score_by_right) # maximum of these two possibilities
            return memo[(left,right)]

        return maxDiff(0,n-1) >=0