class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int start=0, res=0;
        
        map<char,int> d;
        
        
        for (int end=0;end<s.size();end++){
            
            // if element is already seen
            if (d.find(s[end])!=d.end()){
                
                start=max(start,d[s[end]]);
            }
            
            res=max(res,end-start+1);
            d[s[end]]=end+1;
            
        }
        
        return res;
        
    }
};

