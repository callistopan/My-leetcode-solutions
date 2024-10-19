class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case
        if n == 1:
            return "0"
        
        mid = 2**(n-1)  # Middle position of the current binary string
        
        if k == mid:
            return "1"
        elif k < mid:
            return self.findKthBit(n-1, k)
        else:
            # Mirror the k value to the first half and flip the bit
            mirrored_k = 2**n - k
            return "1" if self.findKthBit(n-1, mirrored_k) == "0" else "0"
