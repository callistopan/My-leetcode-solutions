class Solution:
    def maxPoints(self,points):
        m, n = len(points), len(points[0])

        # Initialize dp with the first row
        dp = points[0]

        # Process each row starting from the second row
        for i in range(1, m):
            # Left to right pass
            left_dp = [0] * n
            left_dp[0] = dp[0]  # No cost for the first column
            for j in range(1, n):
                left_dp[j] = max(left_dp[j - 1] - 1, dp[j])

            # Right to left pass
            right_dp = [0] * n
            right_dp[-1] = dp[-1]  # No cost for the last column
            for j in range(n - 2, -1, -1):
                right_dp[j] = max(right_dp[j + 1] - 1, dp[j])

            # Update dp for the current row
            for j in range(n):
                dp[j] = points[i][j] + max(left_dp[j], right_dp[j])

        # The answer is the maximum value in dp after processing all rows
        return max(dp)

        