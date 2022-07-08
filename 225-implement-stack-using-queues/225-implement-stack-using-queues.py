class MyStack:

    def __init__(self):
        self.q1= deque()
        self.q2= deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        
        while len(self.q1)>1:
            top=self.q1.popleft()
            self.q2.append(top)
        
        res=self.q1.pop()
        
        temp=self.q1
        
        self.q1= self.q2
        
        self.q2 =temp
        
        return res

    def top(self) -> int:
        
        if self.q1:
            return self.q1[-1]
        
        
        
        

    def empty(self) -> bool:
        
        if self.q1:
            return False
        
        return True
        
'''
1 2 3 4

4   3
3   2
2   1
1

'''

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()