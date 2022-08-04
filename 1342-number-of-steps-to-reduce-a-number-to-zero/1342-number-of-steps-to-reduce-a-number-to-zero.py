class Solution:
    def numberOfSteps(self, num: int) -> int:
        '''
        14
        
        1110 111 110 11 10 1 0
        '''
        # right shift , if 0 then count+=1 else if it is 1 then count+=2
        
        count=0
        while num:
            
            if num&1:
                count+=2
                
            else:
                count+=1
                
            num>>=1
        return count-1 if count>0 else 0
        