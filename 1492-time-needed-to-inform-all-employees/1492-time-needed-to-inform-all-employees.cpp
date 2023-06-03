class Solution {
public:
    int maxTime = INT_MIN;
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        vector<int> adjList[n];

        for (int i = 0; i < n; i++){
            if (manager[i] != -1){
                adjList[manager[i]].push_back(i);
            }
        }

        queue<pair<int,int>> q;
        q.push({headID,0}); // node and time

        while (!q.empty()){
            pair<int,int> manager = q.front();
            q.pop();

            int parent = manager.first;
            int time = manager.second;
            // update the maximum time
            maxTime = max(maxTime, time);
            for (int adjacent : adjList[parent]){
                q.push({adjacent,time+informTime[parent]});
            }
        }
        return maxTime;
    }
};