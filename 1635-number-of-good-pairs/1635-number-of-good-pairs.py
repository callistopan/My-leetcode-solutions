class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        good_pairs=0
        for key,val in d.items():
            good_pairs+=val*(val-1)//2
        return good_pairs