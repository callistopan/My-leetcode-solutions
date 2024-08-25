class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        c = Counter(s)
        return (c["1"] - 1 )*"1"+ (c["0"] * "0")+"1"