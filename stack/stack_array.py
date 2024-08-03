from typing import TypeVar, Generic, List

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._stack: List[T] = []
        self._size: int = 0

    def push(self, value: T) -> None:
        self._stack = [value] + self._stack
        self._size += 1

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        value = self._stack[0]
        del self._stack[0]
        self._size -= 1
        return value

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self._stack[0]

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def __str__(self) -> str:
        return str(self._stack)
    
