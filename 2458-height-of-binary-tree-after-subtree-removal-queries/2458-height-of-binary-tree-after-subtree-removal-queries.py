class Solution:
    def treeQueries(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        Depth, Height = defaultdict(int), defaultdict(int)
        
        # Pre-compute Depths and Heights
        def dfs(node, depth):
            if not node:
                return -1
            Depth[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            Height[node.val] = cur
            return cur
        dfs(root, 0)
        
        # Group nodes according to their depths
        cousins = defaultdict(list)
        
        for val, depth in Depth.items():
            cousins[depth].append((-Height[val], val))
            cousins[depth].sort()
            if len(cousins[depth]) > 2:
                cousins[depth].pop()
                
        ans = []
        for q in queries:
            depth = Depth[q]
            if len(cousins[depth]) == 1: # no cousins
                ans.append(depth - 1)
            elif cousins[depth][0][1] == q: # q having the largest height
                ans.append(-cousins[depth][1][0] + depth) # return the second largest
            else:
                ans.append(-cousins[depth][0][0] + depth) # return the largest height
        return ans
    
#https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/discuss/2757990/Python-3-Explanation-with-pictures-DFS 
        