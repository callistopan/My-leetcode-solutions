class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k = len(original)
        if m * n != k:
            return []
        res = []
        j = 0
        for i in range(m):
            res.append(original[j:j+n])
            j+= n
        return res