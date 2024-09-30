from collections import Counter

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set('aeiou')
        res = 0
        
        for i in range(n):
            vowel_count = Counter()
            consonants = 0
            for j in range(i, n):
                if word[j] in vowels:
                    vowel_count[word[j]] += 1
                else:
                    consonants += 1
                
                if consonants == k and len(vowel_count) == 5:
                    res += 1
                elif consonants > k:
                    break
        
        return res