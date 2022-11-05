class Solution {
public:
    struct TrieNode{
        vector<TrieNode*> child;
        string word;
        TrieNode(): word(""),child(vector<TrieNode*>(26,nullptr)){}
    };
    
    TrieNode* buildTrie(vector<string>& words){
        TrieNode* root =new TrieNode();
        for (string w: words){
            TrieNode* curr= root;
            for (char c:w){
                int i=c-'a';
                if (curr->child[i]==NULL){
                    curr->child[i]=new TrieNode();
                }
                curr=curr->child[i];
            }
            curr->word=w;
        }
        return root;
    }
    
    
    
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
            vector<string> res;
            TrieNode* root=buildTrie(words);
            for (int i=0;i<board.size();i++){
                for (int j=0;j<board[0].size();j++){
                    dfs(board,i,j,root,res);
                }
            }
        return res;   
        
    }
    void dfs(vector<vector<char>>& board,int i,int j,TrieNode* curr,vector<string>& res){
        char c=board[i][j];
        if (c=='#' or curr->child[c-'a']==NULL) return;
        curr=curr->child[c-'a'];
        if (curr->word !=""){
            res.push_back(curr->word);
            curr->word="";
        }
        board[i][j] = '#';
        if(i > 0) dfs(board, i - 1, j , curr, res); 
        if(j > 0) dfs(board, i, j - 1, curr, res);
        if(i < board.size() - 1) dfs(board, i + 1, j, curr, res); 
        if(j < board[0].size() - 1) dfs(board, i, j + 1, curr, res); 
        board[i][j] = c;
    }
    
    
    
    
    
    
    
    
    
    
    
    
};