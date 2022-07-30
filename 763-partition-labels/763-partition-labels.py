class Solution:
    ''' for each letter encountered process last occurence of letter extend last partition'''
    def partitionLabels(self, S: str) -> List[int]:
        rightmost = {c:i for i, c in enumerate(S)}
        left, right = 0, 0

        result = []
        for i, letter in enumerate(S):

            right = max(right,rightmost[letter])

            if i == right:   # end of current substring
                result += [right-left + 1]
                left = i+1   # increase left for new subsequence

        return result