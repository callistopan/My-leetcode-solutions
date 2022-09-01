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
    int count(TreeNode* root, int curr_max){
        if (root==NULL) return 0;
        int curr=max(root->val,curr_max);
        return (root->val>=curr_max) +count(root->left,curr)+count(root->right,curr);
    }
    int goodNodes(TreeNode* root) {
        return count(root,root->val);
        
    }
    
   
};


