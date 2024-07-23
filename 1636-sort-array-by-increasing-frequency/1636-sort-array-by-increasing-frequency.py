class Solution:
    def frequencySort(self, A: List[int]) -> List[int]:
        count = collections.Counter(A)
        return sorted(A, key=lambda x: (count[x], -x))