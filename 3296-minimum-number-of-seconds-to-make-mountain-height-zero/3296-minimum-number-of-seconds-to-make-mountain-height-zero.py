class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def helper(m):
            total = 0
            for wt in workerTimes:
                l_height = 0
                r_height = mountainHeight
                while l_height < r_height:
                    mid_height = (l_height + r_height + 1) // 2
                    time = wt * mid_height * (mid_height + 1) // 2
                    if time <= m:
                        l_height = mid_height
                    else:
                        r_height = mid_height - 1
                total += l_height
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight

        l_time, r_time = 0, max(workerTimes) * mountainHeight * (mountainHeight +1) //2
        while l_time < r_time:
            mid_time = (l_time + r_time) // 2
            if helper(mid_time):
                r_time = mid_time
            else:
                l_time = mid_time + 1
        return r_time
