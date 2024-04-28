class Solution {
public:
    vector<unordered_set<int>> tree;
    vector<int> res,count;
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        tree.resize(n);
        res.assign(n,0);
        count.assign(n,1); // count stores number of nodes in subtree+ this node

        // generate graph

        for (auto edge : edges){
            tree[edge[0]].insert(edge[1]);
            tree[edge[1]].insert(edge[0]);
        }
        PostOrder(0,-1); // postorder traversal  for updating count and sum of distances in that subtree
        PreOrder(0,-1); // calculate our final answer
        return res;
        

    }
    

    void PostOrder(int root, int pre){
        for (auto i : tree[root]){
            if (i==pre) continue;
            PostOrder(i,root);
            count[root]+=count[i];
            res[root]+=res[i]+count[i];
        }
    }

    void PreOrder(int root, int pre){
        for (auto i : tree[root]){
            if (i==pre) continue;

            res[i]= res[root] - count[i] + count.size() - count[i];  // count.size()==n
            // res[root] - count[i] will find the sum of distances in i subtree + another n- count[i] nodes from i
            PreOrder(i,root);
        }
    }


};












