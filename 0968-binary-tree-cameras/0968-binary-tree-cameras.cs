/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private int cameraCount;
    
    // States
    private const int NEEDS_CAMERA = 0;
    private const int HAS_CAMERA = 1;
    private const int COVERED = 2;
    
    public int MinCameraCover(TreeNode root) {
        cameraCount = 0;
        if (PostOrder(root) == NEEDS_CAMERA){
            cameraCount++;
        }
        return cameraCount;
    }
    
    private int PostOrder(TreeNode node){
        if (node == null){
            return COVERED;
        }
        int left = PostOrder(node.left);
        int right = PostOrder(node.right);
        if (left == NEEDS_CAMERA || right == NEEDS_CAMERA){
            cameraCount++;
            return HAS_CAMERA;
        }
        if (left == HAS_CAMERA || right == HAS_CAMERA){
            return COVERED;
        }
        return NEEDS_CAMERA;
    }
    
}













