class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        '''
        1 ->1 step
        
        10 ->3 step  rule 1-> 11 -> rule 2 -> 01->rule 1 ->00
        11->2step
        100->   rule 1 ->101 ->rule 2 ->111 ->rule 1 ->110 ->
        
        
        '''
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)