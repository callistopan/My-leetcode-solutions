class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.s = []

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.s.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.s:
            res = self.s[-1]
            self.size -=1
            self.s.pop()
            return res
            
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,self.size)):
            self.s[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)