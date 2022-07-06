class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        if right height is greater than left height
        then we are sure that we can store the water in it
        if current left height is more than previous one then we can assign this as maximum
        else there is one possible storage option for water current left max -current height
        
        
        do this for right part also if condition is opposite
        
        '''
        if not height:
            return 0
        l,r=0,len(height)-1
        res=0
        lm,rm=0,0   #leftmax,rightmax
        while l<r:
            if height[l]<height[r]:
                if height[l]>lm:
                    lm=height[l]
                else:
                    res+=lm-height[l]
                l+=1
            else:
                if height[r]>rm:
                    rm=height[r]
                else:
                    res+=rm-height[r]
                r-=1
        return res
                