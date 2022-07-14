class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
        import heapq
        heap=[]
        for col in range(len(matrix[0])):
            heapq.heappush(heap,(matrix[0][col],0,col))
        val=0
        
        # O(klogk)
        for i in range(k):
            val,row,col=heapq.heappop(heap)
            new_val=float('inf')
            if row<len(matrix)-1:
                new_val=matrix[row+1][col]
            heapq.heappush(heap,(new_val,row+1,col))
        return val