from typing import List
from math import inf
'''
time complexity
O(nlogn+nlog(max_value))
'''

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        # Sort the intervals by their starting points
        start.sort()

        # Helper function to check if we can maintain a minimum distance of `mid` between chosen numbers
        def fn(mid):
            # Initialize x to negative infinity to start from a very low point
            x = -inf
            # Iterate over each interval defined by `start`
            for s in start:
                # Increment x by the desired minimum distance `mid`
                x += mid
                # If x is greater than the end of the current interval, it's not possible
                if x > s + d:
                    return False
                # Move x to the maximum between itself and the current start `s`
                x = max(x, s)
            # If all intervals are valid, return True
            return True
        
        # Optimized upper bound for the maximum possible score
        lo, hi = 0, (start[-1] + d) - start[0]  # Set upper bound based on the range of possible values
        
        # Perform binary search to find the maximum possible minimum distance
        while lo < hi:
            # Calculate the mid-point; this is the candidate for the maximum score (minimum distance)
            mid = (lo + hi + 1) >> 1
            # If it's possible to choose numbers with at least `mid` distance apart, move `lo` to `mid`
            if fn(mid):
                lo = mid
            # Otherwise, adjust the high boundary
            else:
                hi = mid - 1
        
        # The result is the largest `lo` for which the function fn(mid) returned True
        return lo
