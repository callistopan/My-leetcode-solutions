class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        
        string ans;
        
        for (int i=0;i<d.size();i++){
            int si=0,di=0;
            for(;si<s.size() && di<d[i].size();si++){
                di+=(s[si]==d[i][di]);
            }
            
            if (di==d[i].size() and (ans.size() <d[i].size() or (ans.size()==d[i].size() and ans>d[i])))
                ans=d[i];
        }
        
        return ans;
    }
};