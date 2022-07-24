class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ''' take right sum as the sum of nums
            increase leftsum and decrease the right sum'''
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            if leftSum == rightSum - nums[i]:
                return i

            leftSum += nums[i]
            rightSum -= nums[i]

        return -1