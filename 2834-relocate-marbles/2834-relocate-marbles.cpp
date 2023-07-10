class Solution {
public:
   vector<int> relocateMarbles(vector<int>& nums, vector<int>& moveFrom, vector<int>& moveTo) {
    set<int> s(begin(nums), end(nums));
    for (int i = 0; i < moveFrom.size(); ++i) {
        s.erase(s.find(moveFrom[i]));// remove from the set as we are moving all marbles
        s.insert(moveTo[i]); // inssert new new position 
    }
    return vector<int>(begin(s), end(s)); // convert set to vector
}
};