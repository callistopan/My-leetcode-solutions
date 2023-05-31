#include <unordered_map>
#include <string>

class UndergroundSystem {
private:
    std::unordered_map<int, std::pair<std::string, int>> checkIns;
    std::unordered_map<std::string, std::pair<double, int>> travelTimes;

public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, std::string stationName, int t) {
        checkIns[id] = std::make_pair(stationName, t);
    }
    
    void checkOut(int id, std::string stationName, int t) {
        std::pair<std::string, int> checkInData = checkIns[id];
        std::string route = checkInData.first + "-" + stationName;
        int travelTime = t - checkInData.second;
        
        if (travelTimes.find(route) != travelTimes.end()) {
            travelTimes[route].first += travelTime;
            travelTimes[route].second++;
        } else {
            travelTimes[route] = std::make_pair(travelTime, 1);
        }
        
        checkIns.erase(id);
    }
    
    double getAverageTime(std::string startStation, std::string endStation) {
        std::string route = startStation + "-" + endStation;
        std::pair<double, int> travelTimeData = travelTimes[route];
        return travelTimeData.first / travelTimeData.second;
    }
};
