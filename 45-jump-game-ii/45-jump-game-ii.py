class Solution:
    def jump(self, A: List[int]) -> int:
        jump_count = 0
        reachable = 0
        curr_reachable = 0
        '''update the current reachable'''
        for i, length in enumerate(A):
            if i > curr_reachable:
                curr_reachable = reachable
                jump_count += 1
            reachable = max(reachable, i + length)
            
        return jump_count