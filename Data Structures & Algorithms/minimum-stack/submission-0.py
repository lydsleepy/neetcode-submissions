class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        heapq.heappush(self.heap, value)

    def pop(self) -> None:
        val = self.stack.pop()
        self.heap.remove(val)
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]
        
