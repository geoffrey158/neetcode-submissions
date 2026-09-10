class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If minStack is empty, this value is automatically the minimum
        # Otherwise, store the smaller of:
        # - the new value
        # - the previous minimum
        if not self.minStack: #stack is empty
            self.minStack.append(val)
        else: #stack is not empty
        #we need to store the old minimum just in case the top element gets poppped and we need to change the minimum
            self.minStack.append(min(self.minStack[-1],val))


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
