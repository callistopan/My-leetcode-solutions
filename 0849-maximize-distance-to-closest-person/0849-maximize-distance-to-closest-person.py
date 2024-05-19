class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [-1] * n
        right = [-1] * n
        
        # Fill the left array
        for i in range(n):
            if seats[i] == 1:
                left[i] = i
            elif i > 0:
                left[i] = left[i - 1]
        
        # Fill the right array
        for i in range(n - 1, -1, -1):
            if seats[i] == 1:
                right[i] = i
            elif i < n - 1:
                right[i] = right[i + 1]
        
        max_dist = 0
        for i in range(n):
            if seats[i] == 0:
                # Distance to the nearest person on the left
                left_dist = float('inf') if left[i] == -1 else i - left[i]
                # Distance to the nearest person on the right
                right_dist = float('inf') if right[i] == -1 else right[i] - i
                # Minimum distance to the nearest person
                min_dist = min(left_dist, right_dist)
                # Update max distance
                max_dist = max(max_dist, min_dist)
        
        return max_dist
                    