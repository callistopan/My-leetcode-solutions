class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack=[]
        
        for i in range(len(nums)):
            
            if not stack:
                
                stack.append(nums[i])
                
            elif (len(stack)%2==0 and nums[i]==stack[-1]) or nums[i]!= stack[-1]:
                
                stack.append(nums[i])
                
        if len(stack)%2==1:
            return len(nums)-len(stack)+1
                
        return len(nums)-len(stack)