/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    void rightview(TreeNode* root,int level,int& max_level,vector<int>& res){
        
        if (root==NULL){
            return; 
        }
        
        if (max_level<level){
            res.push_back(root->val);
            max_level= level;
        }
        
        rightview(root->right,level+1,max_level,res);
        rightview(root->left,level+1,max_level,res);
        
        
    }
    
    vector<int> rightSideView(TreeNode* root) {
        
        int max_level=0;
        vector<int> res;
        rightview(root,1,max_level,res);
        return res;
        
    }
};




