class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
        ''' we push the first row elements to the heap ,O(n) time '''
        import heapq
        heap=[]
        for col in range(len(matrix[0])):
            heapq.heappush(heap,(matrix[0][col],0,col))
        val=0
        
        '''first pop the element from the heap ,element at the top is the minimum element so we are getting minimum                element at k times at the end we are getting the k th smallest elment
           we are actully storing the position of this element in our heap so that we can determine the position of                next element to push.
           
           1  5   9
           
          10  11  13
          
          12  13  15           
           
        
        
        
        ,O(klogk)''' 
        for i in range(k):
            val,row,col=heapq.heappop(heap)
            new_val=float('inf')
            if row<len(matrix)-1:
                new_val=matrix[row+1][col]
            heapq.heappush(heap,(new_val,row+1,col))
        return val