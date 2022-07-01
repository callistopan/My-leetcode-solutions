# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''we push heads of all linked lists to the heap (minheap)'''
        
        heap=[]
        for index, head in enumerate(lists): #O(k)
            if head:
                heap.append((head.val,index))
                
        '''heapify this array'''
        heapq.heapify(heap)   #O(klogk)
        '''creating dummy node'''
        head=current=ListNode(None)
        
        '''we iterate for each and every element ->until the heap is empty'''
        while heap: #O(Nlogk)
            value,index=heapq.heappop(heap)
            '''build our answer :this is the minimum we can get now'''
            current.next=ListNode(value)
            current=current.next
            '''because we are storing the index along with the head'''
            node=lists[index]=lists[index].next
            '''If the next node of this list exists then we have to push to heap
               the heap will automatically heapify '''
            if node:
                heapq.heappush(heap,(node.val,index))
                
        return head.next   #finally :)
        
        
        
        '''time complexity:
                for each node we are popping from heap we may or may not do a heapush operation
                which takes O(log(k)) times to adjest.
                so O(Nlogk)
                O(k) space for the heap
        
        '''
            
            
        