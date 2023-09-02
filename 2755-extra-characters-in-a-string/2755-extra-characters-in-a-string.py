class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n , dictionary_set = len(s) , set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0

            ans = dp(start +1) +1

            for end in range(start ,n):
                current_word = s[start:end+1]

                if current_word in dictionary_set:
                    ans = min(ans, dp(end+1))
            return ans

        return dp(0)