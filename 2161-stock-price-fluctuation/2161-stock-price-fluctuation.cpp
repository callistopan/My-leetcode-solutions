class StockPrice {
public:
    map<int,int> rec; // key= time stamp , val = price 
    multiset<int> count; // store prices
    StockPrice() {
        
    }
    
    void update(int timestamp, int price) {
        if (rec.find(timestamp) != rec.end()){
            count.erase(count.find(rec[timestamp]));  // remove the price at the iterator
        }
        rec[timestamp] =price; // set new price
        count.insert(price); // insert price to multiset
    }
    
    int current() {
        return rec.rbegin()->second; // price for last time stamp
    }
    
    int maximum() {
        return *count.rbegin();  // end of multiset
    }
    
    int minimum() {
        return *count.begin();   // beginning of multiset
    }
};

/**
 * Your StockPrice object will be instantiated and called as such:
 * StockPrice* obj = new StockPrice();
 * obj->update(timestamp,price);
 * int param_2 = obj->current();
 * int param_3 = obj->maximum();
 * int param_4 = obj->minimum();
 */