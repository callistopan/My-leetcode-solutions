class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        if n < 2:
            return [True] * len(queries)
        
        parity_diff = [0] * n
        for i in range(1, n):
            parity_diff[i] = (nums[i] % 2) != (nums[i - 1] % 2)
    
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + parity_diff[i]
        
        result = []
        for fromi, toi in queries:
            if fromi == toi:
                result.append(True)  
            else:
                total_diff_parity = prefix_sum[toi] - prefix_sum[fromi]
                is_special = (total_diff_parity == (toi - fromi))
                result.append(is_special)
        
        return result