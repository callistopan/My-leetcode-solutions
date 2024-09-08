class Solution(object):
    def splitListToParts(self, root, k):
        # Step 1: Count the total number of nodes in the linked list
        cur = root
        N = 0
        while cur:
            N += 1
            cur = cur.next
        
        # Step 2: Determine the size of each part (width) and how many parts will have an extra node (remainder)
        width, remainder = divmod(N, k)
        
        # Step 3: Split the list into parts
        ans = []
        cur = root
        for i in range(k):
            # Start a new part
            head = cur
            # Calculate the correct size for the current part
            part_size = width + (1 if i < remainder else 0)
            
            # Move the pointer to the end of the current part
            for j in range(part_size - 1):
                if cur:
                    cur = cur.next
            
            # If there's a current node, disconnect the end of the current part and move to the next part
            if cur:
                next_part = cur.next
                cur.next = None
                cur = next_part
            
            # Add the current part to the result
            ans.append(head)
        
        return ans
