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
    
    void binaryPaths(TreeNode* root, vector<string>& res, string t){
        
        if (root->left==NULL and root->right==NULL){
            res.push_back(t);
            return;
        }
        if (root->left){
            
            binaryPaths(root->left,res,t+"->"+to_string(root->left->val));
            
            
        }
        if (root->right){
            binaryPaths(root->right,res,t+"->"+to_string(root->right->val));
        }
    }
    
    vector<string> binaryTreePaths(TreeNode* root) {
        
        vector<string> res;
        
        if (root==NULL){
            return res;
        }
        
        binaryPaths(root,res,to_string(root->val));
        
        return res;
    }
};