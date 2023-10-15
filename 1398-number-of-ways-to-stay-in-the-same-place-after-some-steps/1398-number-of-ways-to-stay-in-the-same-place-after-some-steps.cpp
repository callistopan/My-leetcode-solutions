#include <unordered_map>
#include <string>

class Solution {
public:
    int Mod = 1000000007;
    int numWays(int steps, int arrLen) {
        std::unordered_map<std::string, int> memo;
        return dp(0, steps, arrLen, memo);
    }

    long long dp(int pos, int steps, int arrLen, std::unordered_map<std::string, int>& memo) {
        std::string key = std::to_string(pos) + "," + std::to_string(steps);

        if (memo.find(key) != memo.end()) {
            return memo[key];
        }

        if (pos == 0 && steps == 0) {
            return 1;
        }

        if (pos >= arrLen || pos < 0 || steps < 0) {
            return 0;
        }

        long long result = (dp(pos, steps - 1, arrLen, memo) + dp(pos + 1, steps - 1, arrLen, memo) + dp(pos - 1, steps - 1, arrLen, memo)) % Mod;
        memo[key] = result;
        return result;
    }
};
