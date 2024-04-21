class DSU{
    vector<int> parent , rank;

public:
    DSU(int n){
        parent.resize(n);
        rank.resize(n);
        iota(parent.begin(),parent.end(),0) ;// fills from 0,1,2......n-1
        // assigning parents of each node as it is
    }

    int find(int x){  // find the parent
        if(x!=parent[x]){
            parent[x]=find(parent[x]);
        }
        return parent[x];

    }

    bool Union(int x,int y){
        int xp= find(x);
        int yp= find(y);
        if (xp==yp){
            return true;
        }
        else{
            if (rank[xp]>rank[yp]){  // Connect to the higher rank parent
                parent[yp]=xp;
            }
            else if (rank[xp]<rank[yp]){ // connect to higher rank parent
                parent[xp]=yp;
            }
            else{   // ranks are equal
                parent[yp]=xp;
                rank[xp]++;
            }
            return false;
        }
    }
};


class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        DSU uf(n);
        for (int i=0;i<edges.size();i++){
            uf.Union(edges[i][0],edges[i][1]);
        }
        return uf.Union(source,destination);

        
    }
};