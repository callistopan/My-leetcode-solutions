class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def helper(m):
            total = 0
            for wt in workerTimes:
                left_x = 0
                right_x = 2 * (10 ** 12)
                while left_x < right_x:
                    mid = (left_x + right_x + 1) // 2
                    cost = wt * mid * (mid + 1) // 2
                    if cost <= m:
                        left_x = mid
                    else:
                        right_x = mid - 1
                total += left_x
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight

        left, right = 0, max(workerTimes) * mountainHeight * (mountainHeight +1) //2
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left
