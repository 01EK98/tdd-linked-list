from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: float
    next: Optional["Node"] = None


class LinkedList:
    """
    Visualization:
        head           tail
            O -> O -> O
            1    2    3
        head = node1
        tail = node3

        node1.next = node2
        node2.next = node3
        node3.next = None
    """

    head: Optional[Node]
    tail: Optional[Node]
    length: int

    def __init__(self, value: float) -> None:
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.length = 1

    def append(self, value: float) -> None:
        new_node = Node(value)
        if self.length == 0:
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        elif self.length == 1:
            self.tail = new_node
            self.head.next = new_node
        else:
            temp = self.tail
            temp.next = new_node
            self.tail = temp.next
        self.length += 1

    def pop(self) -> None:
        if self.length == 0:
            raise ValueError("This LinkedList instance has no nodes to pop from.")
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            penultimate_node = self.penultimate_node
            self.tail = penultimate_node
            penultimate_node.next = None
        self.length -= 1

    def prepend(self, value: float) -> None:
        new_node = Node(value)
        if self.length == 0:
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        elif self.length == 1:
            temp = self.head
            new_node.next = temp
            self.head = new_node
            self.tail = temp
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
        self.length += 1

    def pop_first(self) -> None:
        if self.length == 0:
            raise ValueError("This LinkedList instance has no nodes to pop from.")
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head.next
            self.head.next = None
            self.head = temp
        self.length -= 1

    @property
    def penultimate_node(self) -> Node:
        penultimate_node = None
        if self.length > 1:
            temp = self.head
            while temp != self.tail:
                penultimate_node = temp
                temp = temp.next
        return penultimate_node
