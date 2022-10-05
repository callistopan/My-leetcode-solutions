class Solution {
public:
    vector<int> diStringMatch(string s) {
        // when I append lowest possible 
        // when D append highest possible
        int n=s.size();
        vector<int> res;
        int low=0,high=n;
        
        for (auto c:s){
            if (c=='I'){
                res.push_back(low);
                low++;
            }
            else{
                res.push_back(high);
                high--;
            }
        }
        res.push_back(low);
        return res;
    }
};