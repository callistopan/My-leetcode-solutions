class LUPrefix {
public:
    LUPrefix(int n) {
        
    }
    set<int> s;
    int z=1;
    
    void upload(int video) {
        s.insert(video);
    }
    
    int longest() {
        
        while (s.find(z)!=s.end()){
            z++;
        }
        return z-1;
        
    }
};

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix* obj = new LUPrefix(n);
 * obj->upload(video);
 * int param_2 = obj->longest();
 */