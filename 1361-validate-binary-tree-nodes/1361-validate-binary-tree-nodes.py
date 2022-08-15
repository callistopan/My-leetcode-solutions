class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find the root node
        
        root=0
        
        children_nodes=set(leftChild+rightChild)
        
        for i in range(n):
            if i not in children_nodes:
                root=i
                
                
        q= deque()
        q.append(root)
        visited=set()
        
        
        while q:
            
            node= q.popleft()
            
            # if node is already visited then we return false as we cannot visit the node in second time
            if node in visited:
                return False
            visited.add(node)
            
            if leftChild[node]!=-1:
                q.append(leftChild[node])
                
            if rightChild[node]!=-1:
                q.append(rightChild[node])
                
        return len(visited)==n
                
        