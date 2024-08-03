from typing import TypeVar

T = TypeVar("T")

class Node:
    def __init__(self, data:T, next=None):
        self.data = data
        self.next = next

class Queue():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def enqueue(self, value: T) -> None:
        node = Node(value, None)

        if self.tail is not None:
            self.tail.next = node
        self.tail = node

        if self.is_empty():
            self.head = node

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        
        value = self.head.data
        self.head = self.head.next

        if(self.head is None):
            self.tail = None

        return value

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.head.data

    def is_empty(self) -> bool:
        return self.head is None

