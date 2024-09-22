class Solution(object):
    def findKthNumber(self, n, k): # n = 13 , k = 2
        curr = 1
        k -= 1
        # curr = 1 , k = 1
        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if step <= k:
                # Move to the next prefix and decrease k by the number of steps we skip
                curr += 1
                k -= step
            else:
                # Move to the next level of the tree and decrement k by 1
                curr *= 10 # curr = 10
                k -= 1 # k = 0

        return curr

    # To count how many numbers exist between prefix1 and prefix2
    def _count_steps(self, n, prefix1, prefix2): #n = 13 prefix1 = 1, prefix2 = 2
        steps = 0
        while prefix1 <= n: # 1 <= 13 10 <= 13
            steps += min(n + 1, prefix2) - prefix1 # 2 - 1 = 1 + (14 - 10) = 5
            prefix1 *= 10
            prefix2 *= 10
        return steps