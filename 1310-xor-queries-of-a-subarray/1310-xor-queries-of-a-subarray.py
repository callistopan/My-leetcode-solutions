class Solution:
    def xorQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        '''
        In-place calculate the prefix XOR of input A.

        For each query [i, j],
        if i == 0, query result = A[j]
        if i != 0, query result = A[i - 1] ^ A[j]
        
        because when we XOR prefix A[j] with A[i-1] the A[i-1] already occurs in A[j] too
        so duplicates will cancel out
        resulting XOR is of query subarray's XOR
        '''
        
        for i in range(len(A) - 1):
            A[i + 1] ^= A[i]
        return [A[j] ^ A[i - 1] if i>0 else A[j] for i, j in queries]
        