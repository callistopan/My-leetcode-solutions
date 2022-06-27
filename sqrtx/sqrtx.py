class Solution:
    def mySqrt(self, x: int) -> int:
        ''' we can deal with 0 and 1 cases separately also'''
        left,right=0,x+1 #for dealing 0,1 cases
        while left<right:
            mid=left+(right-left)//2
            if mid*mid>x:
                right=mid
            else:
                left=mid+1
        return left-1
    
    
    #8   l=0 and r=9 