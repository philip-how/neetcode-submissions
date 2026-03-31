class MinStack:

    def __init__(self):
        self.real_stack = []
        self.lowest_stacks = []
        

    def push(self, val: int) -> None:
        self.real_stack.append(val)
        if len(self.lowest_stacks) == 0 or val <= self.lowest_stacks[-1]:
            self.lowest_stacks.append(val)
        

    def pop(self) -> None:
        top = self.real_stack.pop()
        if top == self.lowest_stacks[-1]:
            self.lowest_stacks.pop()       

    def top(self) -> int:
        return self.real_stack[-1]
        

    def getMin(self) -> int:
        return self.lowest_stacks[-1]
        
