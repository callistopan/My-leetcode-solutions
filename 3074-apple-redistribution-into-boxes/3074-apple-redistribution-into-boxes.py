class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        count = 0
        capacity.sort(reverse = True)
        currentTotal = 0
        
        for c in capacity:
            currentTotal += c
            count += 1
            if currentTotal >= total:
                return count
            