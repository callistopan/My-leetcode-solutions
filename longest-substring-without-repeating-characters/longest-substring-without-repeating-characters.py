class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map={}
        start,res=0,0
        for end in range(len(s)):
            if s[end] in map:   #if element is already seen
                start=max(map[s[end]],start)
            res=max(res,end-start+1)
            map[s[end]]=end+1  #store for future reference so that we can update the start
        return res
            
        