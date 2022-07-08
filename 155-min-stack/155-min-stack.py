class MinStack:

    def __init__(self):
        self.s = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.s.append((x, curMin));


    def pop(self):
        self.s.pop()

    def top(self):
        if len(self.s) == 0:
            return None
        else:
            return self.s[-1][0]


    # @return an integer
    def getMin(self):
        if len(self.s) == 0:
            return None
        else:
            return self.s[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()