class Solution:
    # time complexity O(a+b+c) 
    # space O(1)
    def longestDiverseString(self,a: int, b: int, c: int) -> str:
        result = []
        counts = [(a, 'a'), (b, 'b'), (c, 'c')]

        while True:
            counts.sort(reverse=True) # higest to lowest eg: a=5 b=3 c=2
            if counts[0][0] == 0: # there is nothing left
                break
            # violates the 3 substring proprerty then choose the next highest char
            if len(result) >= 2 and result[-1] == counts[0][1] and result[-2] == counts[0][1]: 
                if counts[1][0] == 0: # no next highest char
                    break
                result.append(counts[1][1]) 
                counts[1] = (counts[1][0] - 1, counts[1][1]) # update the count of second highest
            # no violation of any property just append the highest freq character to result
            else:
                result.append(counts[0][1])  
                counts[0] = (counts[0][0] - 1, counts[0][1]) 

        return ''.join(result)
