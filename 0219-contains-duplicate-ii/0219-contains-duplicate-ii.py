class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table={}
        
        for i in range(len(nums)):
            if nums[i] not in hash_table:
                hash_table[nums[i]]=i
            else:
                if abs(hash_table[nums[i]]-i)<=k:
                    return True
                hash_table[nums[i]]=i
        return False
                