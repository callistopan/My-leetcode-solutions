class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        s = dict(sorted(d.items(),key=lambda x:x[1],reverse = True))
        res=[]
        for i in s.keys():
            k-=1
            res.append(i)
            if k==0:
                return res