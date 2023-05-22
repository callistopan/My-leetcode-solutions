class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket, res = [[] for _ in range(len(nums) + 1)], []
        for a, b in Counter(nums).items():
            bucket[b].append(a)
        print(bucket)
        for l in bucket[::-1]:
            if len(l): res += l
            if len(res) >= k: return res[ : k]