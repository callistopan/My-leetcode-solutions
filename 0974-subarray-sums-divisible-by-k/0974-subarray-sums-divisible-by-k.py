class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''a sum divisible by k means sum of zero modulo k
           dictionary counts number of prefix sumsmodulo k
           subtracting prefix sum from running sum makes a subarray of sum 0 modulo k
           VERY TRICKY'''
        result=0
        running_sum=0
        prefix_sum=defaultdict(int)
        prefix_sum[0]=1

        for num in nums:
            running_sum=(running_sum+num)%k
            result+=prefix_sum[running_sum]
            prefix_sum[running_sum]+=1
        return result