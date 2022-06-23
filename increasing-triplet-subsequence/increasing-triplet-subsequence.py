class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstSmall = secondSmall = float('inf')
        for num in nums:
            if num<=firstSmall:
                firstSmall = num
            elif num<=secondSmall:
                secondSmall = num
            else:
                return True
        return False