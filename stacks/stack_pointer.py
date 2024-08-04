from typing import TypeVar, Generic, List

T = TypeVar("T")

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack():
    def __init__(self) -> None:
        self.top = None

    def push(self, value: T) -> None:
        node = Node(value, None)
        node.next = self.top
        self.top = node

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data

    def is_empty(self) -> bool:
        return self.top == None
