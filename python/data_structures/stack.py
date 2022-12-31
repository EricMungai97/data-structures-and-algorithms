from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        # Adds node to the top of the stack
        if self.top is None:
            self.top = Node(value)
            return
        old = self.top
        self.top = Node(value)
        self.top.next = old

    def pop(self):
        # Remove top node from stack, Returns value of removed node.
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        popped = self.top
        self.top = self.top.next
        return popped.value

    def peek(self):
        # Returns True if stack is empty, otherwise return False
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        # Return True if stack is empty, else return False
        if self.top:
            return False
        else:
            return True

