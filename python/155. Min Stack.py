class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.min_val = []

    def push(self, x: int) -> None:
        self.nums.append(x)
        if len(self.min_val) == 0:
            self.min_val.append(x)
        else:
            min_v_tmp = self.min_val[-1] if self.min_val[-1] < x else x
            self.min_val.append(min_v_tmp)
        

    def pop(self) -> None:
        if len(self.nums) != 0:
            self.nums.pop(-1)
            self.min_val.pop(-1)
        

    def top(self) -> int:
        return self.nums[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()