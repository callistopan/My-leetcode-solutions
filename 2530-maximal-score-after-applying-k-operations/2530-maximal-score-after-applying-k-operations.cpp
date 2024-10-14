#include <queue>
class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int, vector<int>> pq;
        for (int i : nums) {
        pq.push(i);
    }

        long long score=0;

        for (int i=0;i<k;i++){
            long long top = pq.top();
            pq.pop();
            score+=top;
            top= ceil(double(top)/3);
            pq.push(top);
        }

        return score;
    }
};