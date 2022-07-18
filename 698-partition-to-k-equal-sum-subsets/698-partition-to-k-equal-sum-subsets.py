class Solution:
    def canPartitionKSubsets(self,nums: List[int], k: int) -> bool:
        '''as we are partioning to k equal partion we any partion has greater than sum(nums)//k sum then we cannot proceed''' 
        sums = [0]*k
        subsum = sum(nums) / k
        nums.sort(reverse=True)
        l = len(nums)
        
        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False        
        
        return walk(0)
        
#         nums_sum = sum(nums)
#         if nums_sum % k != 0:
#             return False
#         subset_sum = nums_sum // k
        
#         ks = [0] * k
#         nums.sort(reverse=True)
        
    
#         def can_partition(j):
#             if j == len(nums):
#                 for i in range(k):
#                     if ks[i] != subset_sum:
#                         return False
#                 return True
#             for i in range(k):
#                 if ks[i] + nums[j] <= subset_sum:
#                     ks[i] += nums[j]
#                     if can_partition(j + 1):
#                         return True
#                     ks[i] -= nums[j]
                
                    
#             return False

#         return can_partition(0)
                
                
                
        
        
        
        
        
        
        