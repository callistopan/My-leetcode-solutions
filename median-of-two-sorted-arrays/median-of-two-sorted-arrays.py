class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        
            2 4 6
            
            1 3 5 7 8
            
            
            1 2 3 4 5 6 7 8  =>4.5
        
        
        * There are two sorted arrays nums1 and nums2 of size m and n respectively.
     * Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
     *
     * Solution
     * Take minimum size of two array. Possible number of partitions are from 0 to m in m size array.
     * Try every cut in binary search way. When you cut first array at i then you cut second array at (m + n + 1)/2 - i
     * Now try to find the i where a[i-1] <= b[j] and b[j-1] <= a[i]. So this i is partition around which lies the median.
     *
     * Time complexity is O(log(min(x,y))
     * Space complexity is O(1)
        
        '''
        
        if len(nums1)> len(nums2):
            
            return self.findMedianSortedArrays(nums2,nums1)
        
        x = len(nums1)   # we use this for binary search
        
        y = len(nums2)
        
        
        low =0
        
        high =x
        
        while low <= high:
            
            partitionX = (low+high)//2
            
            partitionY = (x+y+1)//2 - partitionX
            
            '''if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX'''
            '''if partitionX is length of input then there is nothing on right side. Use +INF for minRightX'''
            
            maxLeftX = nums1[partitionX-1] if partitionX!=0 else float("-inf")
            
            minRightX = nums1[partitionX] if partitionX != x else float("inf")
            
            maxLeftY = nums2[partitionY-1] if partitionY !=0 else float("-inf")
            
            minRightY = nums2[partitionY] if partitionY  != y else float("inf")
            
            
            if (maxLeftX <= minRightY and maxLeftY <= minRightX):
                '''
                //We have partitioned array at correct place
                // Now get max of left elements and min of right elements to get the median in case of even length combined array size
                // or get max of left for odd length combined array size.
                
                '''
                if (x+y)%2==0:
                    
                    return (max(maxLeftX,maxLeftY) +min(minRightX,minRightY))/2
                
                else:
                    
                    return max(maxLeftX,maxLeftY)
                
            elif maxLeftX > minRightY :  # go to left
                
                high = partitionX -1
                
            else:
                
                low =partitionX +1
                
                
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        