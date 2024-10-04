class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        ans, sum_ = 0, 0
        l, r = 0, n - 1
        for i in range(n//2):
            if i == 0:
                sum_ += skill[l] + skill[r]
                ans += (skill[l] * skill[r])
            else:
                if ( skill[l] + skill[r]) != sum_:
                    return -1
                ans += (skill[l]* skill[r])
            l +=1
            r -=1
        return ans