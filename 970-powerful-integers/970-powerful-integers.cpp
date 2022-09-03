class Solution {
public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        if (bound==0){
            return vector<int>();
        }
        int n=x>1 ? log10(bound)/log10(x):0;
        int m=y>1 ? log10(bound)/log10(y):0;
        vector<int>res;
        
        
        for (int i=0;i<=n;i++){
            for(int j=0;j<=m;j++){
                if (pow(x,i)+pow(y,j)<=bound){
                    res.push_back(pow(x,i)+pow(y,j));
                }
            }
        }
        set<int> s( res.begin(), res.end() );
        vector<int> vec;
        vec.assign( s.begin(), s.end() );
        return vec;
    }
};