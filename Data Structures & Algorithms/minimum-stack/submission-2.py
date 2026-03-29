class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()
    

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        queue = []
        minimum = float("inf")
        for _ in range(len(self.stack)):
            data = self.stack.pop()
            minimum = min(data, minimum)
            queue.append(data)
        for _ in range(len(queue)):
            self.stack.append(queue.pop())
        return int(minimum)
        
