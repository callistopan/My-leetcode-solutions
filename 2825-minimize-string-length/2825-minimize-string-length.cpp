class Solution {
public:
    int minimizedStringLength(string s) {
        set<char> st;
        for (auto c:s){
            st.insert(c);
        }
        return st.size();
        
    }
};