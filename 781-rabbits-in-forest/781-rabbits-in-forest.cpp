class Solution {
public:
    int numRabbits(vector<int>& answers) {
       unordered_map<int, int> c;
        for (int i : answers) c[i]++;
        int res = 0;
        for (auto i : c) res += (i.second + i.first) / (i.first + 1) * (i.first + 1);
        return res;
    }
};

/*

0 0 1 1 1

here 3 rabbits answered as 1 so first rabbit know there is one another rabbit of same color => let 1 1 be red=2
other rabbit know there is one more of same colour let it be 1 =2
0 0 =>2
generally there is 3 rabbits have said 1 
so there is like 3/2+1 groups here x=1 x+1=2 (generally)
if it is 3 3 3 => 3/4+1 =>1 group 
33333 5/4+1=2 groups





*/