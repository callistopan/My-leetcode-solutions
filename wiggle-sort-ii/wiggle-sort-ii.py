class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        half = len(nums[::2])
        print(half)
        print(nums[:half][::-1])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
        '''
        put the smaller half on even indices
        and the larger half on odd indices
        so they are  well placed 
        solution is O(nlogn)
        '''
        
        
        

            
            
            
            
            
    