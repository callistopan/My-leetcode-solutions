class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
            sort the intervals
            if the list of merged intervals is empty or if current interval is not 
            overlapping then  we have to append to our result
            if overlapping is found then we have to find the largest of the previous interval
            last element and current element interval last element 
            
        '''
        intervals.sort(key =lambda x: x[0])
        merged =[]
        for i in intervals:
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged