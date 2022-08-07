class Solution:
    '''
    O(26*len(s))
    '''
    def removeDuplicateLetters(self, s: str) -> str:
        
        rindex = {c: i for i, c in enumerate(s)}
        print(rindex)
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while result and c < result[-1] and i < rindex[result[-1]]:  # we can remove the last element of the result if current character is less than result[-1] and there is an appearance of result[-1] onn right 
                    result = result[:-1]
                result += c
        return result