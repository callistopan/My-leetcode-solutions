class Solution:
    def minPartitions(self, n: str) -> int:
        max_num=float("-inf")
        for i in n:
            if i=='9':
                return 9
            if int(i)>max_num:
                max_num=int(i)
        return  max_num