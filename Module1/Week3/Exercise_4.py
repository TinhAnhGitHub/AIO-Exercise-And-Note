class Queue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.list = []

    def is_empty(self) -> bool:
        return len(self.list) == 0
    
    def is_full(self) -> bool:
        return len(self.list) == self.capacity
    
    def dequeue(self) -> None:
        assert not self.is_empty(), "The list is empty"
        del self.list[0]
    def enqueue(self, value: int) -> None:
        assert not self.is_full(), "The list is full"
        self.list.append(value)
    
    def front(self) -> int:
        return self.list[0] if not self.is_empty() else None