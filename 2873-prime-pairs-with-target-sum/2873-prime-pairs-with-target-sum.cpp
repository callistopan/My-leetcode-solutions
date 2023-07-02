vector<int> p;  // store all the prime numbers 
class Solution
{
    public:
        vector<vector < int>> findPrimePairs(int n)
        {
            if (p.empty())
            {
                bool sieve[1000000] = {}; 
                for (long long i = 2; i < 1000000; ++i)
                    if (!sieve[i])
                    {
                        p.push_back(i);
                        for (long long j = i * i; j < 1000000; j += i)
                            sieve[j] = true;
                    }
            }
            vector<vector < int>> res;
            int i = 0, j = upper_bound(begin(p), end(p), n) - begin(p) - 1;// we need upto n
           // binary search entire prime numbers for suitable x + y == n 
            while (i <= j)
            {
                if (p[i] + p[j] == n)
                {
                    res.push_back({ p[i],
                        p[j] });
                    ++i, --j;
                }
                else if (p[i] + p[j] < n)
                    ++i;
                else
                    --j;
            }
            return res;
        }
};