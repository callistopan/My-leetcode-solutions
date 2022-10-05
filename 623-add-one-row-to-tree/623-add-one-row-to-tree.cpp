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
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth==1){
            TreeNode* n=new TreeNode(val);
            n->left=root;
            return n;
            
        }
        insert(root,val,1,depth);
        return root;
    }
    
    void insert(TreeNode* root,int val,int depth,int n){
        if (!root) return;
        if (depth==n-1){
            TreeNode* t = root->left;
            root->left=new TreeNode(val);
            root->left->left=t;
            
            t=root->right;
            root->right=new TreeNode(val);
            root->right->right=t;
            
        }
        else{
            insert(root->left,val,depth+1,n);
            insert(root->right,val,depth+1,n);
        }
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
};