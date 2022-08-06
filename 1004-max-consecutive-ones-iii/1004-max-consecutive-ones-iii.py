class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        '''
        if right pointer have '0' then we decrease the k
        
        if k<0 means we have so many 0's so we need to adjest our sliding window
        
        '''
        max_len=0
        left = right = 0
        for right in range(len(A)):
            print(left,right)
            if A[right] == 0: 
                K -= 1
            print("K="+str(K))
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            max_len= max(right-left+1,max_len)
            
        return max_len