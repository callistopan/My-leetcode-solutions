class Solution:
    def longestDiverseString(self,a: int, b: int, c: int) -> str:
        result = []
        counts = [(a, 'a'), (b, 'b'), (c, 'c')]

        while True:
            counts.sort(reverse=True)
            if counts[0][0] == 0:
                break
            if len(result) >= 2 and result[-1] == counts[0][1] and result[-2] == counts[0][1]:
                if counts[1][0] == 0:
                    break
                result.append(counts[1][1])
                counts[1] = (counts[1][0] - 1, counts[1][1])
            else:
                result.append(counts[0][1])
                counts[0] = (counts[0][0] - 1, counts[0][1])

        return ''.join(result)
