class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = nums.size();
        vector<long long> res (n,0);

        unordered_map<int,vector<int>> d;
        for (int i = 0; i < n; i++){
            d[nums[i]].push_back(i);
        }

        for (auto it : d){
            int num = it.first;
            vector<int>& indexes = it.second;

            long long totalSum = 0;
            for (int index : indexes){
                totalSum += (long long )index;
            }
            long long preSum = 0;

            long long total_sum = 0;
            for (int i = 0 ; i < indexes.size() ; i++){
                int index = indexes[i];
                long long postSum = totalSum - preSum - index;

                // i - p1 + i- p2 .....
                res[index] += (index* (long long )i); // pre sum all i s
                res[index] -= (preSum);  // substract all the prev indexes

                // a1 - i + a2 -i + ...

                res[index] -= (index* (long long)(indexes.size()-i-1)); // pre sum all i s
                res[index] += (postSum);

                preSum += index;

            }
        }

        return res;
    }
};