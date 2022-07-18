class Node:
    
    def __init__(self, k, v):  ###3 each nodes
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)   #fake node linked together in doubly liknked list fasion
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):   # find our key
        if key in self.dic:  # if key is present in our dictionary
            n = self.dic[key]
            self._remove(n)  # remove from linked list and 
            self._add(n)     # add to the tail of linked list for most recently used
            return n.val
        return -1

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)    # add at the end of linked list 
        self.dic[key] = n  # add to dictionary
        if len(self.dic) > self.capacity:
            n = self.head.next  #  removing from front that is least recently used
            self._remove(n)
            del self.dic[n.key]   ###removing from our dictionary beacause there is no enough space to accomodate it
#removing from list whenever get called and it's placed at end of list (most recently used)
    def _remove(self, node): # remove from linked list
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):####adds at end of linked list so that its most recently used
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)