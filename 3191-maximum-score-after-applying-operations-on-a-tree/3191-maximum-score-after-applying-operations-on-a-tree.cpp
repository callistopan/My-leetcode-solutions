class Solution {
public:
    long long maximumScoreAfterOperations(vector<vector<int>>& edges, vector<int>& values) {
        vector<vector<int>> tree(values.size());
        for (auto e : edges){
            tree[e[0]].push_back(e[1]);
            tree[e[1]].push_back(e[0]);
        }
        return dfs(tree, values , 0 ,-1).first;
        
    }

    pair<long , long> dfs( vector<vector<int>> & tree, vector<int> & values , int node ,int parent){
        long long leftout = 0 , taken = 0;
        for (auto c : tree[node]){
            if (c== parent) continue;
            auto [t,l] = dfs(tree, values,c ,node);
            taken += t ;
            leftout +=l;
        }

        taken += (leftout !=0) ? max(leftout, (long long)values[node]): 0;
        leftout = (leftout !=0)? min(leftout,(long long)values[node]): values[node];
        return { taken, leftout};
    }
};