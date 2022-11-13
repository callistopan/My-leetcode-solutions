class Solution {
public:
    void reverseword(string &s,int l,int r){
        while (l<r){
            char temp= s[l];
            s[l++]=s[r];
            s[r--]=temp;
        }
    }
    string reverseWords(string s) {
        int i=0,j=0,l=0,wordcount=0;
        int n= s.size();
        
        
        while (true){
            while (i<n and s[i]==' ')i++;
            if (i==n) break;
            if (wordcount) s[j++]=' ';
            l=j;
            
            while (i<n and s[i] !=' '){
                s[j]=s[i];
                j++;
                i++;
                
            }
            reverseword(s,l,j-1);
            wordcount++;
        }
        s.resize(j);
        reverseword(s,0,j-1);
        return s;
    }
};