from typing import TypeVar, Generic, List

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._queue: List[T] = []
        self._size: int = 0
    
    def enqueue(self, value:T) -> None:
        self._queue = self._queue + [value]
        self._size += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
            return
        value = self._queue[0]
        del self._queue[0]
        self._size -= 1
        return value
    
    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
            return
        return self._queue[0]

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        return str(self._queue)