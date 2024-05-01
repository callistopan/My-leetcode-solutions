class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first_index = -1
        word = list(word)
        n = len(word)
        for i in range(n):
            if word[i] == ch:
                first_index = i
                break
        if first_index != -1:
            l = 0
            r = first_index
            while l<= r:
                t = word[l]
                word[l] = word[r]
                word[r] = t
                l+=1
                r-=1
        return ''.join(word)
        