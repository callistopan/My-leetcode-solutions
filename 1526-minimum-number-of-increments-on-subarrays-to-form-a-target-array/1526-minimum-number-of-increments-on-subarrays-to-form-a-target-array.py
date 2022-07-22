'''
Whenever the current element a is bigger than the previous element,
we need at lease a - pre operations to make this difference.

We accumulate the total number of the operations,
this result is a lower bound and it's feasible.
'''

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for a in target:
            res += max(a - pre, 0)
            pre = a
        return res