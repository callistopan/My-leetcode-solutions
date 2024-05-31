class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        print(xor)
        mask = 1
        while(xor&mask == 0):#find first set bit
            mask = mask << 1
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]