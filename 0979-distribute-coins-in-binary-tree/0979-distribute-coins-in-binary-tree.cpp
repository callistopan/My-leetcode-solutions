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
    //  we should push coins from parents to it's child so we just return the number of coins needs
    // to be pushed from parent to child
    int ans =0;
    
    int dfs(TreeNode* root){
        if (root==NULL){
            return 0;
        }
        
        int left = dfs(root->left);
        int right= dfs(root->right);
        
        ans+=abs(left)+abs(right);
        return root->val+left+right-1;
    }
    
    int distributeCoins(TreeNode* root) {
        
        int a=dfs(root);
        return ans;
    }
};