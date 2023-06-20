class Solution
{
    public:
        vector<int> getAverages(vector<int> &nums, int k)
        {
            int n = nums.size();
            vector<int> res(n, -1);
           
           	// prefix
            vector<long long> prefix(n, 0);
            for (int i = 1; i < n; i++)
            {
                prefix[i] = prefix[i - 1] + nums[i - 1];
            }

            for (int i = k; i < n - k; i++)
            {
                res[i] = (nums[i + k] + prefix[i + k] - prefix[i - k]) / (2 *k + 1);
            }

            return res;
        }
};

// valid 2k + 1 elements
// start from the index k up to n-k
// calculate the prefix and suffix sum of array 
//      ......i-k....i......i+k  sum = prefix[i+k] + nums[i+k] - prefix[i-k]
// average = sum/2k+1