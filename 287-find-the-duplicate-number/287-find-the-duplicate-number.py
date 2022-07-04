class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        
        for i in range(n):
            
            if nums[abs(nums[i])]<0:
                return abs(nums[i])
            
            nums[abs(nums[i])]*=-1
            
#         # Find the intersection point of the two runners.
#         tortoise = hare = nums[0]
#         while True:
#             tortoise = nums[tortoise]
#             hare = nums[nums[hare]]
#             if tortoise == hare:
#                 break
        
#         # Find the "entrance" to the cycle.
#         tortoise = nums[0]
#         while tortoise != hare:
#             tortoise = nums[tortoise]
#             hare = nums[hare]
        
#         return hare
            
            
            
        
        