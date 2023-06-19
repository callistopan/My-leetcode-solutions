class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int highest_altitude = 0;
        int sum = 0;

        for (int i = 0 ; i < gain.size(); i++){
            sum += gain[i];
            highest_altitude = max(highest_altitude,sum);

        }
        return highest_altitude;
    }
};