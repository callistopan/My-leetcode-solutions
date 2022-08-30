class Solution {
public:
    // the idea is to generate all possible permutations of the given sequence optimally
    
    int count=0;
    int countArrangement(int n) {
        vector<bool> visited(n+1,0);
        backtrack(n,1,visited);
        return count;
    }
    
    void backtrack(int n,int pos, vector<bool>& visited){
        if (pos>n){
            count++;
        }
        
        for(int i=1;i<=n;i++){
            if (!visited[i] and (pos%i==0 or i%pos==0)){
                visited[i]=true;
                backtrack(n,pos+1,visited);
                visited[i]=false;
            }
        }
    }
};