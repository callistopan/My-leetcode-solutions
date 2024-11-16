from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []

        # Iterate through each subarray of size k
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            
            # Check if the sorted subarray contains consecutive numbers
            is_consecutive = True
            for j in range(1, k):
                if subarray[j] != subarray[j - 1] + 1:
                    is_consecutive = False
                    break
            
            if is_consecutive:
                results.append(subarray[-1])
            else:
                results.append(-1)
        
        return results
