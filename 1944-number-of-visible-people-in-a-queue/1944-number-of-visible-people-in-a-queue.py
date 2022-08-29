class Solution:
    def canSeePersonsCount(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        stack = []
        for i, v in enumerate(A):
            while stack and A[stack[-1]] <= v:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
        return res
    
    '''
    res = 3 1 2 1 0 0
    10 -stack=0
    6  - stack[-1]=0   stack=0 1
    8  - stack=0 2 stack[-1]=0 
    5  - stack=0 2 3
    11 - stack= empty
    9  - nothing
    
    
    '''