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
    string getDirections(TreeNode* root, int startValue, int destValue) {
        string s_p, d_p; // start path and destination path
        find(root, startValue, s_p);
        find(root, destValue, d_p);

        while (!s_p.empty()  && !d_p.empty() && s_p.back() == d_p.back()){
            // remove prefixes
            s_p.pop_back();
            d_p.pop_back();
        }
        return string(s_p.size(),'U') + string(rbegin(d_p),rend(d_p)); 
    }

    bool find(TreeNode* n, int val, string& path ){
        if (n->val == val){
            return true;
        }
        if (n->left && find(n->left, val, path)){
            path.push_back('L');
        }
        else if (n->right && find(n->right,val, path)){
            path.push_back('R');
        }
        return !path.empty();
    }
};







