class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1 and maxDoubles > 0:
            res += 1 + (target % 2)   # even one step odd two steps
            maxDoubles -= 1
            target >>= 1
        return res + target - 1 # we need to continuously decrease from target to 1
    
    
    
    '''
    Intuition

    We should use double action as late as possible, as many as possible.
    Do this process reversely: Reduce target to 1.
    We try to use the HALF action as soon as possbile..

    Explanation

    If we still "half" action, we do it.
    If it's odd, we decrese it by 1 and make it half, which takes two actions.
    If it's even, we make it half, which takes one action.

    If no more "half" action, we decrement continuously to 1, which takes target - 1        actions.
    
    
    
    
    '''