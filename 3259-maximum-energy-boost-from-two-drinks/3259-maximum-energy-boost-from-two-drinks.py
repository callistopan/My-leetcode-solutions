class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        
        @cache
        def dfsA(i):
            if i>= n:
                return 0
            return energyDrinkA[i] + max(dfsA(i + 1), dfsB(i + 2))
        @cache
        def dfsB(i):
            if i >= n:
                return 0
            return energyDrinkB[i] + max(dfsB(i + 1), dfsA( i + 2))
        return max(dfsA(0), dfsB(0))