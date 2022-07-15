class Solution:
    ''' first create an array sub for storing our elements
        we iterate over the array and for each element we need to find the position of this element         in our sub array
        - use binary search for this 
        - if position returned is same as the len of sub array then this is a new larger element
          so we can just append the element to our sub array
          
        - else there is a valid point to insert ,so just insert the element into that position
        
        -2,3,7,101 of lenght 4
        
        10,9,2,5,3,7,101,18
        
        sub =[2,3,18,101] 
        
        
        '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        #tails array is always sorted 
        def binarySearch(sub, val):
            lo, hi = 0, len(sub)-1
            while(lo <= hi):
                mid = lo + (hi - lo)//2
                if sub[mid] < val:
                    lo = mid + 1
                elif val < sub[mid]:
                    hi = mid - 1
                else:
                    return mid
            return lo
        
        sub = []
        for val in nums:
            pos = binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)