class Solution {
public:
    int maxNumberOfBalloons(string text) {
        std::unordered_map<char, int> counts;
        int result = INT_MAX;

        for (char c : text) {
            counts[c]++;
        }

        std::unordered_map<char, int> balloonCount{
            {'b', 1},
            {'a', 1},
            {'l', 2},
            {'o', 2},
            {'n', 1}
        };

        for (auto it = balloonCount.begin(); it != balloonCount.end(); ++it) {
            char c = it->first;
            int count = it->second;
            result = std::min(result, counts[c] / count);
        }

        return result;
    }
};