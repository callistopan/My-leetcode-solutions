class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> res;
        res.push_back(first);
        
        for (auto n:encoded){
            res.push_back(first^n);
            first^=n;
        }
        return res;
    }
};